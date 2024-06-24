import platform
import os
import zipfile
import json

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QThread, pyqtSignal, QProcess
from qfluentwidgets import FluentIcon
import wget

from .ui_ip_check import Ui_FormIpCheck

GOOGLE_TRANSLATE_IP_CHECK_PATH = 'GoogleTranslateIpCheck'
system = {'Windows': 'win', 'Linux': 'linux', 'Darwin': 'osx'}[platform.system()]


class ThreadDownload(QThread):
    """下载GoogleTranslateIpCheck的线程"""
    sig_bar = pyqtSignal(int, int, int)
    sig_success = pyqtSignal()
    sig_failed = pyqtSignal(BaseException)

    def __init__(self, parent: "InterfaceIpCheck"):
        super().__init__(parent=parent)
        self.ui = parent

    def run(self):
        # 创建文件夹
        if not os.path.exists(GOOGLE_TRANSLATE_IP_CHECK_PATH):
            os.mkdir(GOOGLE_TRANSLATE_IP_CHECK_PATH)

        # 下载文件
        url = f'https://github.com/Ponderfly/GoogleTranslateIpCheck/releases/download/1.8/{system}-x64.zip'
        if self.ui.checkBox_moeyy.isChecked():  # 国内加速
            url = 'https://github.moeyy.xyz/' + url
        try:
            wget.download(url, f'{GOOGLE_TRANSLATE_IP_CHECK_PATH}/', self.sig_bar.emit)
        except BaseException as e:
            self.sig_failed.emit(e)
            return
        # 解压文件
        with zipfile.ZipFile(f'{GOOGLE_TRANSLATE_IP_CHECK_PATH}/{system}-x64.zip', 'r') as zip_ref:
            zip_ref.extractall(f'{GOOGLE_TRANSLATE_IP_CHECK_PATH}/')
        # 删除压缩包
        os.remove(f'{GOOGLE_TRANSLATE_IP_CHECK_PATH}/{system}-x64.zip')

        # 写入数据文件
        with open('data/data.json', 'r') as f:
            data = json.load(f)
        data['gtic_downloaded'] = True
        with open('data/data.json', 'w') as f:
            json.dump(data, f, indent=2)

        self.sig_success.emit()


class InterfaceIpCheck(QWidget, Ui_FormIpCheck):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.init_ui()

        # 下载文件的线程，保证生命周期
        self.thread_download = ThreadDownload(self)
        # GoogleTranslateIpCheck的子进程，保证生命周期
        self.process_gtic = QProcess(self)

        self.connect()

    def init_ui(self):
        """初始化UI"""
        # 检查是否已下载GoogleTranslateIpCheck
        with open('data/data.json', 'r') as f:
            data = json.load(f)
            if data['gtic_downloaded']:
                self.download_finished()
        # 暂停进度条
        self.indeterminateProgressBar_run.pause()
        # 添加图标
        self.pushButton_download.setIcon(FluentIcon.DOWNLOAD)
        self.primaryPushButton_run.setIcon(FluentIcon.SEARCH)

    def connect(self):
        """连接信号与槽"""
        # 界面
        self.pushButton_download.clicked.connect(self.download)  # 下载按钮
        self.primaryPushButton_run.clicked.connect(self.run)  # 运行按钮
        # 下载线程
        self.thread_download.sig_bar.connect(self.bar_adaptive)  # 更新下载进度条
        self.thread_download.sig_success.connect(self.download_finished)  # 下载完成
        self.thread_download.sig_failed.connect(self.download_failed)  # 下载出错
        # GoogleTranslateIpCheck子进程
        self.process_gtic.readyReadStandardOutput.connect(
            lambda: self.plainTextEdit_output.appendPlainText(
                self.process_gtic.readAllStandardOutput().data().decode('gbk')
            )
        )  # 实时输出
        self.process_gtic.finished.connect(self.run_finished)  # 运行完成

    def download(self):
        """下载GoogleTranslateIpCheck"""
        self.set_download_enabled(False)
        # 子线程，启动！
        self.thread_download.start()

    def bar_adaptive(self, current, total, width=80):
        """更新进度条的函数"""
        self.progressBar_download.setMaximum(total)
        self.progressBar_download.setValue(current)

    def download_finished(self):
        """下载完成后要做的事"""
        # 调整按钮
        self.set_download_enabled(False)
        self.set_run_enabled(True)
        # 拉满进度条
        self.bar_adaptive(100, 100)

    def download_failed(self, e: BaseException):
        """下载出错"""
        # 启用下载一栏
        self.set_download_enabled(True)
        # 截停进度条
        self.progressBar_download.error()
        raise e

    def set_download_enabled(self, enabled: bool):
        """设置下载一栏的可用性"""
        self.pushButton_download.setEnabled(enabled)
        self.checkBox_moeyy.setEnabled(enabled)

    def set_run_enabled(self, enabled: bool):
        """设置运行一栏的可用性"""
        self.primaryPushButton_run.setEnabled(enabled)
        self.checkBox_IPv6.setEnabled(enabled)
        self.checkBox_s.setEnabled(enabled)

    def run(self):
        """运行GoogleTranslateIpCheck"""
        self.set_run_enabled(False)
        self.indeterminateProgressBar_run.resume()
        # 根据系统组装命令
        working_dir = f'{GOOGLE_TRANSLATE_IP_CHECK_PATH}/{system}-x64'
        if system != 'win':
            os.system(f'chmod +x {working_dir}/GoogleTranslateIpCheck')
            command = f'sudo {working_dir}/GoogleTranslateIpCheck -y'
        else:
            command = f'{working_dir}/GoogleTranslateIpCheck.exe -y'
        # 读取勾选项
        command += ' -6' if self.checkBox_IPv6.isChecked() else ''
        command += ' -s' if self.checkBox_s.isChecked() else ''

        # 子进程，启动！
        self.process_gtic.setWorkingDirectory(working_dir)
        self.process_gtic.start(command)

    def run_finished(self):
        """运行完成后要做的事"""
        self.set_run_enabled(True)
        self.indeterminateProgressBar_run.pause()
