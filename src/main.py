import sys
import traceback
import logging
from types import TracebackType
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, FluentTranslator, FluentIcon, NavigationItemPosition, MessageBox

import interfaces
from src.core import gtn_modified

__version__ = '4.0.0-pre3'
gtn_modified.DEBUG_WITHOUT_TRANSLATING = False


class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'谷歌生草机 {__version__}')
        self.setWindowIcon(QIcon(':/img/icon.png'))
        self.resize(800, 600)

        # 添加子界面
        self.ui_translate = interfaces.InterfaceTranslate(self)
        self.addSubInterface(self.ui_translate, FluentIcon.HOME, '生草')
        self.ui_web = interfaces.InterfaceWeb(self)
        self.addSubInterface(self.ui_web, FluentIcon.WIFI, '网页生草')
        self.ui_settings = interfaces.InterfaceSettings(self)
        self.addSubInterface(self.ui_settings, FluentIcon.SETTING, '设置', NavigationItemPosition.BOTTOM)
        self.ui_about = interfaces.InterfaceAbout(self)
        self.addSubInterface(self.ui_about, FluentIcon.INFO, '关于', NavigationItemPosition.BOTTOM)

        # 指定错误日志路径
        logging.basicConfig(filename='错误日志.txt', encoding='utf-8')
        # 自己处理报错
        sys.excepthook = self.excepthook

    def excepthook(self, etype: type[BaseException], value: BaseException, tb: TracebackType):
        """弹窗报错，记录日志"""
        # 获取字符串
        error_str = ''.join(traceback.format_exception(etype, value, tb))
        print(error_str)
        # 写入日志
        logging.exception('错误', exc_info=(etype, value, tb))
        # 弹窗
        w = MessageBox('错误', f'{etype.__name__}: {value}', self)
        if w.exec():
            if etype == gtn_modified.IPCheckError:
                os.system('start https://gt.hzchu.top/ipcheck/')


# 启用高分辨率缩放 enable hidpi scale
QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)
app = QApplication(sys.argv)
# 国际化
qfw_translator = FluentTranslator()
app.installTranslator(qfw_translator)
window = Window()
window.show()
sys.exit(app.exec())
