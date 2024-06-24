import random
from typing import Never

from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from qfluentwidgets import FluentIcon, MessageBox, MessageBoxBase, PlainTextEdit
from aiogoogletrans import LANGUAGES
from gtts import gTTS

from .ui_translate import Ui_FormTranslate
import translate

if __name__ == '__main__':
    from ..main import WindowGGGM


class ThreadTranslate(QThread):
    """生草线程"""
    sig_progress = pyqtSignal(int, str, list)
    sig_success = pyqtSignal()
    sig_failed = pyqtSignal(BaseException)

    def __init__(self, parent: "InterfaceTranslate"):
        super().__init__(parent=parent)
        self.ui = parent

    def run(self):
        # 读取数据
        times = self.ui.spinBox_times.value()
        timeout = self.ui.doubleSpinBox_timeout.value()
        text_list = self.ui.text_list

        # 设置超时
        translate.timeout = timeout

        # 循环翻译
        src = 'auto'
        for i in range(times):
            # 随机目标语言，最后一次翻回中文
            dest = random.choice(self.ui.win.interface_settings.selected_langs) if i != times - 1 else 'zh-cn'
            # 报告进度
            self.sig_progress.emit(i, f'{"自动检测" if i == 0 else LANGUAGES[src]} -> {LANGUAGES[dest]}', text_list)
            try:
                # 翻译
                text_list = self.retry_to_translate(text_list, dest=dest, src=src)
            except BaseException as e:
                self.sig_failed.emit(e)
                return
            # 这次的目标语言为下一次的源语言
            src = dest
        self.sig_progress.emit(times, f'chinese (simplified)', text_list)
        self.sig_success.emit()

    def retry_to_translate(self, text_list: list[str], dest, src) -> list[str] | Never:
        """重试直到成功，不超过一定次数"""
        for _ in range(self.ui.spinBox_retry.value() + 1):
            try:
                return translate.translate_batch(text_list, dest=dest, src=src)
            except BaseException as e:
                e0 = e
        raise e0


class MsgBoxShowText(MessageBoxBase):
    """显示指定文本的弹窗"""

    def __init__(self, text: str, parent):
        super().__init__(parent=parent)
        self.plainTextEdit = PlainTextEdit()
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(text)
        self.plainTextEdit.setMinimumSize(600, 400)
        self.viewLayout.addWidget(self.plainTextEdit)


class ThreadDownloadMp3(QThread):
    """下载音频的线程"""
    sig_success = pyqtSignal(str)
    sig_failed = pyqtSignal(BaseException)

    def __init__(self, parent: "InterfaceTranslate"):
        super().__init__(parent=parent)
        self.ui = parent
        self.path = None

    def run(self):
        text = '\n'.join(self.ui.text_list)
        tts = gTTS(text, lang='zh-cn')
        try:
            tts.save(self.path)
            self.sig_success.emit(self.path)
        except BaseException as e:
            self.sig_failed.emit(e)


class InterfaceTranslate(QWidget, Ui_FormTranslate):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.win: "WindowGGGM" = parent

        self.init_ui()

        # 生草线程，保证生命周期
        self.thread_translate = ThreadTranslate(self)
        # 下载音频的线程，保证生命周期
        self.thread_mp3 = ThreadDownloadMp3(self)

        # 连接信号与槽
        self.connect()

    def init_ui(self):
        # 拉伸表头
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        # 设置按钮图标
        self.primaryPushButton_start.setIcon(FluentIcon.LANGUAGE)
        self.pushButton_manage.setIcon(FluentIcon.ALIGNMENT)
        self.pushButton_all.setIcon(FluentIcon.MENU)
        self.pushButton_121.setIcon(FluentIcon.CHAT)
        self.pushButton_mp3.setIcon(FluentIcon.DOWNLOAD)

    def connect(self):
        """连接信号与槽"""
        self.pushButton_manage.clicked.connect(self.manage_text)
        self.primaryPushButton_start.clicked.connect(self.start_translating)
        self.pushButton_mp3.clicked.connect(self.download_mp3)
        self.pushButton_all.clicked.connect(self.show_all_text)
        self.pushButton_121.clicked.connect(self.show_121_text)
        # 生草线程
        self.thread_translate.sig_progress.connect(self.show_progress)
        self.thread_translate.sig_success.connect(self.translate_finished)
        self.thread_translate.sig_failed.connect(self.translate_failed)
        # 下载音频线程
        self.thread_mp3.finished.connect(lambda: self.pushButton_mp3.setEnabled(True))
        self.thread_mp3.sig_success.connect(
            lambda path: MessageBox('音频下载成功', f'音频已保存到{path}', self.win).exec())
        self.thread_mp3.sig_failed.connect(self.raise_error)

    def manage_text(self):
        """组织文本写入表格中"""
        text = self.plainTextEdit.toPlainText()
        # 分割文本，但保留分隔符
        for sep in self.lineEdit_sep.text():
            text = text.replace(sep, f'{sep}\n')
        text_list = text.split('\n')
        # 删除冗余字符串
        text_list = [line.strip() for line in text_list if line.strip() != '']

        # 写入表格
        self.tableWidget.setRowCount(len(text_list))
        for i, line in enumerate(text_list):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(line))

    @property
    def text_list(self) -> list[str]:
        """源文本列表"""
        return [self.tableWidget.item(i, 0).text() for i in range(self.tableWidget.rowCount())]

    @property
    def translated_text_list(self) -> list[str]:
        """生草文本列表"""
        return [self.tableWidget.item(i, 1).text() for i in range(self.tableWidget.rowCount())]

    def start_translating(self):
        """开始生草"""
        # 禁用自己
        self.setEnabled(False)
        # 设置进度条最大值
        self.progressBar.setMaximum(self.spinBox_times.value())
        # 子线程，启动！
        self.thread_translate.start()

    def show_progress(self, progress: int, lang: str, text_list: list[str]):
        """
        根据当前进度更新界面
        :param progress: 当前已翻译次数
        :param lang: 源语言 -> 目标语言
        :param text_list: 文本列表
        :return: None
        """
        # 更新进度条
        self.progressBar.setVal(progress)
        # 更新语言标签
        self.bodyLabel_lang.setText(lang)
        # 更新表格
        for i, line in enumerate(text_list):
            self.tableWidget.setItem(i, 1, QTableWidgetItem(line))

    def translate_finished(self):
        """生草完成后要做的事"""
        # 启用自己
        self.setEnabled(True)
        # 拉满进度条
        self.progressBar.setVal(self.progressBar.maximum())
        # 弹窗
        w = MessageBox('生草完成', '生草完成', self.win)
        w.exec()

    def translate_failed(self, e: BaseException):
        """翻译出错"""
        # 启用自己
        self.setEnabled(True)
        # 截停进度条
        self.progressBar.error()
        # 向上报告
        raise e

    def show_text(self, text: str):
        """显示指定文本"""
        w = MsgBoxShowText(text, self.win)
        w.exec()

    def show_all_text(self):
        """显示连续文本"""
        self.show_text('\n'.join(self.translated_text_list))

    def show_121_text(self):
        """显示对照文本"""
        text = ''
        for src, dst in zip(self.text_list, self.translated_text_list):
            text += f'{src}\n-> {dst}\n\n'
        self.show_text(text)

    def download_mp3(self):
        """下载音频"""
        path = QFileDialog.getSaveFileName(self.win, '下载音频', None, 'MP3文件 (*.mp3)')[0]
        if path:
            # 禁用自己
            self.pushButton_mp3.setEnabled(False)
            # 子线程，启动！
            self.thread_mp3.path = path
            self.thread_mp3.start()

    def raise_error(self, e: BaseException):
        raise e
