from PySide6.QtCore import QThread
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon, MessageBox
import pyperclip

from .ui_translate import Ui_Translate
from src.core.translate import ThreadManager, State
from src.core import translate

if __name__ == '__main__':
    from main import Window


class InterfaceTranslate(QWidget, Ui_Translate):
    def __init__(self, parent: "Window" = None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(self.__class__.__name__)
        self.window = parent

        # gif
        self.gif = QMovie(':/img/loading.gif')

        # 初始化界面
        self.init_ui()

        # 翻译线程
        self.thread_mgr = ThreadManager(self.window)

        # 连接信号与槽
        self.connect_signal_to_slot()

    def init_ui(self):
        """初始化界面"""
        # 按钮图标
        self.PrimaryPushButton_start.setIcon(FluentIcon.PLAY)
        self.PushButton_ctrl_c.setIcon(FluentIcon.COPY)
        self.PushButton_ctrl_v.setIcon(FluentIcon.PASTE)
        self.PushButton_download_mp3.setIcon(FluentIcon.DOWNLOAD)
        # gif
        self.ImageLabel.setMovie(self.gif)
        self.gif.stop()

    def connect_signal_to_slot(self):
        """连接信号与槽"""
        # 开始翻译
        self.PrimaryPushButton_start.clicked.connect(self.start_translating)
        # 翻译线程
        self.thread_mgr.sig_output.connect(self.PlainTextEdit_output.setPlainText)
        self.thread_mgr.sig_progress.connect(self.ProgressBar.setVal)
        self.thread_mgr.sig_info.connect(self.TransparentPushButton_info.setText)
        self.thread_mgr.sig_timer.connect(self.SubtitleLabel_timer.setText)
        self.thread_mgr.finished.connect(self.end_translating)
        # 一键粘贴
        self.PushButton_ctrl_v.clicked.connect(lambda: self.PlainTextEdit_input.setPlainText(pyperclip.paste()))
        # 一键复制
        self.PushButton_ctrl_c.clicked.connect(self.ctrl_c)

    def ctrl_c(self):
        """一键复制的槽函数"""
        pyperclip.copy(self.PlainTextEdit_output.toPlainText())
        w = MessageBox('一键复制', '已将内容复制到剪切板', self.window)
        w.exec()

    def set_enabled(self, enabled: bool):
        """禁用/启用界面上的可互动组件"""
        self.setEnabled(enabled)
        self.window.ui_web.setEnabled(enabled)
        self.window.ui_settings.setEnabled(enabled)

    def divide_text(self) -> list[str]:
        """
        按句号和换行分割文本
        :return: 文本的列表
        """

        def is_meaningful(s: str) -> bool:
            """
            判断字符串是否有意义
            :param s: 字符串
            :return: 若有意义则为True，反之False
            """
            for i in s:
                if i not in ' \n':
                    return True
            return False

        text = self.PlainTextEdit_input.toPlainText()
        if self.RadioButton_together.isChecked():
            # 整体翻译
            return [text]
        # 逐句翻译
        text = text.replace('。', '\n').split('\n')
        text = [i for i in text if is_meaningful(i)]
        return text

    def start_translating(self):
        """开始翻译，主按钮的槽函数"""
        # 弹窗询问
        self.thread_mgr.text_list = self.divide_text()
        total_times = self.SpinBox_times.value() * len(self.thread_mgr.text_list)
        w = MessageBox('开始生草', f'预计请求次数：{total_times}\n确定要开始吗？', self.window)
        if w.exec():
            # 禁用窗口
            self.set_enabled(False)
            # 设置进度条
            self.ProgressBar.setMaximum(total_times)
            self.ProgressBar.setVal(0)
            # 开启gif
            self.gif.start()
            # 线程，启动！
            self.thread_mgr.start()
            # 提升线程优先级
            self.thread_mgr.setPriority(QThread.Priority.TimeCriticalPriority)

    def end_translating(self):
        """翻译线程停止后执行该函数"""
        # 启用窗口
        self.set_enabled(True)
        # 停止gif
        self.gif.stop()
        # 根据状态弹窗
        match self.thread_mgr.state:
            case State.SUCCESSFUL:
                w = MessageBox('生草完成', '生草完成', self.window)
                w.exec()
            case State.FAILED:
                raise translate.error[1][1]
