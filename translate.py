import random
from copy import deepcopy
import time
import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from google_trans_new import LANGUAGES as LANGUAGES_ALL
from google_trans_new.google_trans_new import google_new_transError

from gtn_modified import GoogleTranslator

if __name__ == '__main__':
    import main

# 联合国六大语言
LANGUAGES_6_KEYS = ['zh-cn', 'fr', 'ru', 'en', 'es', 'ar']
# 用来读取的字典
LANGUAGES_TO_READ = deepcopy(LANGUAGES_ALL)
LANGUAGES_TO_READ['auto'] = '检测语言'
LANGUAGES_TO_READ['zh-cn'] = '简体中文'
LANGUAGES_TO_READ['fr'] = '法语'
LANGUAGES_TO_READ['ru'] = '俄语'
LANGUAGES_TO_READ['en'] = '英语'
LANGUAGES_TO_READ['es'] = '西班牙语'
LANGUAGES_TO_READ['ar'] = '阿拉伯语'

# 报错类型对照字典
ERROR_DICT = {
    ValueError: '请检查输入的值是否合法',
    google_new_transError: '请求超时，请检查网站或代理是否可用或加大超时限制',
    AssertionError: '朗读内容为空',
    FileNotFoundError: '文件路径错误',
}


class ThreadTranslateOne(QThread):
    def __init__(self, text, window):
        super().__init__()
        self.window: "main.Window" = window
        self.text = text
        self.progress = 0
        self.info = 'None'
        self.error = [False, ()]

    def run(self):
        try:
            self.translate()
        except Exception:
            self.error = [True, sys.exc_info()]

    def translate(self):
        # 读取参数
        url_base = self.window.ui_t.LineEdit_url_base.text()
        times = self.window.ui_t.SpinBox_times.value()
        timeout = self.window.ui_t.SpinBox_timeout.value()
        if self.window.ui_s.CheckBox_proxies.isChecked():
            proxies = {
                'http': self.window.ui_s.LineEdit_http.text(),
                'https': self.window.ui_s.LineEdit_https.text()
            }
        else:
            proxies = None

        # 翻译
        translator = GoogleTranslator(url_base, timeout, proxies)
        for i in range(times):
            # 第一次自动检测源语言
            if i == 0:
                src = 'auto'
            # 随机选择语言
            tgt = self.choose_lang()
            if i == times - 1:
                tgt = 'zh-cn'
            # 汇报信息
            self.info = f'[{self.progress}/{times}] {LANGUAGES_TO_READ[src]} -> {LANGUAGES_TO_READ[tgt]}'
            # 翻译
            func = lambda: translator.translate(self.text, lang_src=src, lang_tgt=tgt,
                                                cookies=self.window.ui_s.LineEdit_cookies.text())
            self.text = self.keep_retrying(func)
            # print(self.text)
            # 将这次的目标语言设为下次的源语言
            src = tgt
            # 汇报进度
            self.progress = i + 1

    def choose_lang(self) -> str:
        """随机选择语言"""
        index = self.window.ui_s.ComboBox_lang.currentIndex()
        if index == 0:
            return random.choice(list(LANGUAGES_ALL.keys()))
        elif index == 1:
            return random.choice(LANGUAGES_6_KEYS)

    def keep_retrying(self, func):
        """出错后自动重试"""
        for i in range(self.window.ui_t.SpinBox_retry.value() + 1):
            try:
                text = func()
            except Exception as e:
                error = e
            else:
                return text
        raise error


class ThreadStartTranslating(QThread):
    """整体翻译与逐句翻译共用一个逻辑"""
    sig_pb_sv = pyqtSignal(int)  # ProgressBar.setVal
    sig_pb_sm = pyqtSignal(int)  # ProgressBar.setMaximum
    sig_pteo_spt = pyqtSignal(str)  # PlainTextEdit_output.setPlainText
    sig_tpbi_st = pyqtSignal(str)  # TransparentPushButton_info.setText
    sig_error = pyqtSignal(type, Exception, object)
    sig_success = pyqtSignal()

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.divided_texts = []
        self.threads_list = []
        self.info = '未翻译'

    def run(self):
        try:
            self.translate()
        except Exception:
            self.sig_error.emit(*sys.exc_info())

    def translate(self):
        # 初始化（不准偷懒用__init__()！！！）
        self.divided_texts = []
        self.threads_list = []
        self.threads_list = []
        self.info = '未翻译'

        # 读取文本
        text: str = self.window.ui_t.PlainTextEdit_input.toPlainText()
        # 按翻译模式划分文本
        if self.window.ui_t.RadioButton_together.isChecked():
            self.divided_texts = [text]
        elif self.window.ui_t.RadioButton_sentences.isChecked():
            self.divided_texts = text.replace('\n', '。').split('。')
            # 去除无用元素
            self.divided_texts = [i for i in self.divided_texts if self.is_useful(i)]

        # 启动子线程
        self.start_threads()
        # 保持输出
        self.output()

    @staticmethod
    def is_useful(text: str) -> bool:
        """判断字符串是否有用"""
        for i in text:
            if i not in ' \n':
                return True
        return False

    def start_threads(self):
        """给每个句子创建一个线程并启动"""
        self.threads_list = []
        for i in self.divided_texts:
            thread = ThreadTranslateOne(i, self.window)
            thread.start()
            self.threads_list.append(thread)

    def output(self):
        """循环输出结果"""
        # 初始化进度条
        maximum = self.window.ui_t.SpinBox_times.value() * len(self.threads_list)
        self.sig_pb_sv.emit(0)
        self.sig_pb_sm.emit(maximum)
        # 设置显示信息
        self.sig_tpbi_st.emit(f'生草中... 线程数量：{len(self.threads_list)}')
        while True:
            time.sleep(0.05)
            # 设置进度条和输出文本框和显示信息
            progress = 0
            text = ''
            info = ''
            for i in self.threads_list:
                progress += i.progress
                text += f'{i.text}\n'
                info += f'{i.info}\n'
            self.info = info[:-1]
            self.sig_pb_sv.emit(progress)
            self.sig_pteo_spt.emit(text[:-1])
            QApplication.processEvents()

            # 报错检测
            for i in self.threads_list:
                if i.error[0]:
                    self.sig_error.emit(*i.error[1])
                    return None

            # 判断是否完成
            if progress == maximum:
                self.sig_tpbi_st.emit('生草完成')
                self.info = '生草完成'
                self.sig_success.emit()
                return None
