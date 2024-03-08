from typing import Callable
import sys
import random
import time
from enum import Enum, unique
from types import TracebackType

from PySide6.QtCore import QThread, QThreadPool, QRunnable, Signal

from .gtn_modified import GoogleTranslator
from .languages import *

if __name__ == '__main__':
    from main import Window

# 全局变量
current_text_list: list[str] = []
error: list[bool | tuple] = [False, ()]
total_progress: int = 0
finished_thread_cnt: int = 0


class ThreadTranslateOne(QRunnable):
    def __init__(self, window: "Window", func: Callable[[str, str, str], str], idx: int):
        """
        翻译一句话的线程
        :param window: window
        :param func: 翻译的函数，应接受3个参数：文本，源语言，目标语言，返回翻译后的文本
                     代理和cookies应自己设置好
        :param idx: 线程的编号，操作全局列表用的索引
        """
        super().__init__()
        self.window = window
        self.func = func
        self.idx = idx

    def run(self):
        global error
        try:
            self.work()
        except:
            error = [True, sys.exc_info()]

    def work(self):
        global total_progress, finished_thread_cnt
        # 确定语言列表
        match self.window.ui_settings.ComboBox_lang.currentIndex():
            case 0:
                languages = ALL
            case 1:
                languages = UN6

        # 读取次数，开始生草
        times = self.window.ui_translate.SpinBox_times.value()
        for i in range(times):
            text = current_text_list[self.idx]  # 从全局变量中获取自己的文本
            if i == 0:  # 第一次自动检测源语言
                src = 'auto'
            tgt = random.choice(languages)  # 随机目标语言
            text = self.keep_retrying(text, src, tgt)  # 翻译
            current_text_list[self.idx] = text  # 写入全局列表
            total_progress += 1  # 总进度+1（经测试，这一操作在Python3.11中是安全的）
            src = tgt  # 这次的目标语言作为下一次的源语言

        # 完成的线程数+1
        finished_thread_cnt += 1

    def keep_retrying(self, text: str, src: str, tgt: str) -> str:
        """
        执行self.func，但是会自动重试
        :param text: 文本
        :param src: 源语言
        :param tgt: 目标语言
        :return: 翻译后的文本
        """
        retry_times = self.window.ui_translate.SpinBox_retry.value()
        for i in range(retry_times + 1):
            try:
                text = self.func(text, src, tgt)
            except BaseException as e:
                e0 = e
            else:
                return text
        raise e0


@unique
class State(Enum):
    TRANSLATING = 0
    SUCCESSFUL = 1
    FAILED = 2


class ThreadManager(QThread):
    sig_error = Signal(type, BaseException, TracebackType)  # 报错
    sig_output = Signal(str)  # 输出文本
    sig_progress = Signal(int)  # 更新进度条
    sig_info = Signal(str)  # 线程信息
    sig_timer = Signal(str)  # 计时器

    def __init__(self, window: "Window"):
        """翻译的总的线程，会创建并管理子线程进行翻译，并输出结果"""
        super().__init__()
        self.window = window
        self.text_list = []  # 源文本列表
        self.state = State.TRANSLATING

    def run(self):
        global current_text_list, error, total_progress, finished_thread_cnt
        # 初始化全局变量
        current_text_list.clear()
        error = [False, ()]
        total_progress = 0
        finished_thread_cnt = 0
        # 初始化自己
        self.state = State.TRANSLATING

        # 读取参数
        # 镜像网站
        url_base = self.window.ui_settings.SearchLineEdit_url_base.text()
        # 超时
        timeout = self.window.ui_translate.SpinBox_timeout.value()
        # 代理
        if self.window.ui_settings.CheckBox_proxies.isChecked():
            proxies = {
                'http': self.window.ui_settings.LineEdit_http.text(),
                'https': self.window.ui_settings.LineEdit_https.text(),
                'socks5': self.window.ui_settings.LineEdit_socks5.text(),
            }
        else:
            proxies = None
        # cookies
        cookies = self.window.ui_settings.LineEdit_cookies.text()
        cookies = cookies if len(cookies) > 0 else None
        # 初始化谷歌翻译引擎
        translator = GoogleTranslator(url_base, timeout, proxies)
        func = lambda text, src, tgt: translator.translate(text, tgt, src, cookies=cookies)

        # 创建线程池，生命周期仅在该函数内
        pool = QThreadPool()
        pool.setThreadPriority(QThread.Priority.LowestPriority)
        # 设置线程数量上限
        pool.setMaxThreadCount(self.window.ui_settings.SpinBox_max_thread_cnt.value())
        # 将文本复制给全局列表
        current_text_list = self.text_list.copy()

        task_list = []  # 保证线程存活的列表
        # 创建线程并提交给线程池
        for i in range(len(self.text_list)):
            task = ThreadTranslateOne(self.window, func, i)
            task_list.append(task)
            pool.start(task)

        # 不断输出并检测完成或出错
        t0 = time.time()
        while True:
            # 输出结果
            self.sig_output.emit('\n'.join(current_text_list))
            # 更新进度条
            self.sig_progress.emit(total_progress)
            # 显示信息
            active_cnt = pool.activeThreadCount()
            waiting_cnt = len(task_list) - active_cnt - finished_thread_cnt
            self.sig_info.emit(f'{active_cnt}线程运行中\t{waiting_cnt}等待中\t{finished_thread_cnt}已完成')
            # 计时器
            self.sig_timer.emit(format_time(time.time() - t0))

            # 检测完成
            if self.window.ui_translate.ProgressBar.getVal() == self.window.ui_translate.ProgressBar.maximum():
                self.state = State.SUCCESSFUL
                return
            # 检测报错
            if error[0]:
                self.state = State.FAILED
                return

            # 防止cpu爆掉
            time.sleep(0.1)


def format_time(t: float) -> str:
    """
    把时间格式化成时:分:秒:小数点后两位
    例：66.6 -> 00:01:06.60
    :param t: 时间，浮点数
    :return: 格式化后的字符串
    """
    h = int(t / 3600)
    m = int(t % 3600 / 60)
    s = int(t % 60)
    ms = int(t * 100 % 100)
    return f'{h:02d}:{m:02d}:{s:02d}.{ms:02d}'
