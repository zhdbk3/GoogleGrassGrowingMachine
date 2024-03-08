from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from qfluentwidgets import FluentIcon

from .ui_about import Ui_About
import qrc_img

if __name__ == '__main__':
    from main import Window


class InterfaceAbout(QWidget, Ui_About):
    def __init__(self, parent: "Window" = None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName(self.__class__.__name__)
        self.window = parent

        # 初始化界面
        self.init_ui()

    def init_ui(self):
        """初始化界面"""
        # 按钮图标
        self.HyperlinkButton_mczhdbk.setIcon(FluentIcon.LINK)
        self.HyperlinkButton_xdedan.setIcon(FluentIcon.LINK)
        self.HyperlinkButton_thun888.setIcon(FluentIcon.LINK)
        self.HyperlinkButton_statistics.setIcon(FluentIcon.PIE_SINGLE)
        self.HyperlinkButton_github.setIcon(FluentIcon.GITHUB)
        # 头像
        self.AvatarWidget_mczhdbk.setPixmap(QPixmap(':/img/MC着火的冰块.png').scaled(40, 40))
        self.AvatarWidget_xdedan.setPixmap(QPixmap(':/img/薛定谔的按钮.png').scaled(40, 40))
        self.AvatarWidget_thun888.setPixmap(QPixmap(':/img/thun888.png').scaled(40, 40))
