import sys
import os
import json
import traceback
from types import TracebackType

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from qfluentwidgets import FluentWindow, FluentIcon, FluentTranslator, NavigationItemPosition

import interfaces
import img.qrc_img

__version__ = '4.0.0-pre2'


class WindowGGGM(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'谷歌生草机 {__version__}')
        self.setWindowIcon(QIcon(':/icon.png'))
        self.resize(800, 600)

        # 创建数据文件
        if not os.path.exists('data'):
            os.mkdir('data')
            with open('data/data.json', 'w') as f:
                json.dump({'gtic_downloaded': False}, f, indent=2)

        # 添加子界面
        self.interface_translate = interfaces.InterfaceTranslate(self)
        self.addSubInterface(self.interface_translate, FluentIcon.LANGUAGE, '生草主页')
        self.interface_ip_check = interfaces.InterfaceIpCheck(self)
        self.addSubInterface(self.interface_ip_check, FluentIcon.SEARCH_MIRROR, 'GoogleTranslateIpCheck')
        self.interface_settings = interfaces.InterfaceSettings(self)
        self.addSubInterface(self.interface_settings, FluentIcon.SETTING, '设置', NavigationItemPosition.BOTTOM)
        self.interface_about = interfaces.InterfaceAbout(self)
        self.addSubInterface(self.interface_about, FluentIcon.INFO, '关于与帮助', NavigationItemPosition.BOTTOM)

        # 自己处理报错
        sys.excepthook = self.excepthook

    def excepthook(self, etype: type[BaseException], value: BaseException, tb: TracebackType):
        formatted = ''.join(traceback.format_exception(etype, value, tb))
        print(formatted)
        QMessageBox.critical(self, '错误', formatted)


app = QApplication(sys.argv)
qfw_translator = FluentTranslator()
app.installTranslator(qfw_translator)
window = WindowGGGM()
window.show()
sys.exit(app.exec())
