import time
import os

import pyperclip
from qfluentwidgets import MessageBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal

from gtts_modified import GTTS


def ctrl_v(window):
    text = pyperclip.paste()
    window.ui_t.PlainTextEdit_input.setPlainText(text)


def ctrl_c(window):
    text = window.ui_t.PlainTextEdit_output.toPlainText()
    pyperclip.copy(text)
    # 弹窗提醒
    w = MessageBox('一键复制', '已将内容复制到剪切板', window)
    w.exec()


# def download_mp3(window):
#     # 获取路径
#     path = QFileDialog.getSaveFileName(window, '下载音频', None, 'MP3文件(*.mp3)')[0]
#     # 下载音频
#     text = window.ui_t.PlainTextEdit_output.toPlainText()
#     tts = GTTS(text, 'zh-cn', window.ui_t.LineEdit_url_base.text())
#     tts.save(path)
#     # 弹窗提醒
#     w = MessageBox('下载音频', '音频已保存到' + path, window)
#     w.exec()


class ThreadTimer(QThread):
    sig_slt_st = pyqtSignal(str)  # SubtitleLabel_timer.setText

    def __init__(self):
        super().__init__()
        self.running = True

    def run(self):
        self.running = True
        t1 = time.time()
        while self.running:
            t2 = time.time()
            delta_t = t2 - t1
            h = str(int(delta_t // 3600)).zfill(2)
            m = str(int(delta_t % 3600 // 60)).zfill(2)
            s = str(int(delta_t % 60)).zfill(2)
            f = str(int(delta_t % 1 * 100)).zfill(2)  # float
            self.sig_slt_st.emit(f'用时 {h}:{m}:{s}.{f}')
            time.sleep(0.01)

    def turn_off(self):
        self.running = False


class ThreadDownloadMP3(QThread):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.path = None

    def set_path(self):
        self.path = QFileDialog.getSaveFileName(self.window, '下载音频', None, 'MP3文件(*.mp3)')[0]

    def msgbox(self):
        w = MessageBox('下载音频', '音频已保存到' + self.path, self.window)
        w.exec()

    def run(self):
        # 等待path里有值
        while self.path is None:
            time.sleep(0.01)
        # 下载音频
        text = self.window.ui_t.PlainTextEdit_output.toPlainText()
        tts = GTTS(text, 'zh-cn', self.window.ui_t.LineEdit_url_base.text())
        tts.save(self.path)
