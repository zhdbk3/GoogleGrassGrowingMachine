from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from qfluentwidgets import FluentIcon

from .ui_about import Ui_FormAbout


class InterfaceAbout(QWidget, Ui_FormAbout):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.init_ui()

    def init_ui(self):
        # 设置头像
        self.avatarWidget_zhdbk.setPixmap(QPixmap(':/MC着火的冰块.png').scaled(40, 40))
        self.avatarWidget_dinger.setPixmap(QPixmap(':/薛定谔的按钮.png').scaled(40, 40))
        self.avatarWidget_thun888.setPixmap(QPixmap(':/thun888.png').scaled(40, 40))
        # 设置按钮图标
        self.hyperlinkButton_gituhb_repo.setIcon(FluentIcon.GITHUB)
        self.hyperlinkButton_github_zhdbk.setIcon(FluentIcon.GITHUB)
        self.hyperlinkButton_github_dinger.setIcon(FluentIcon.GITHUB)
        self.hyperlinkButton_bilibili_zhdbk.setIcon(FluentIcon.LINK)
        self.hyperlinkButton_bilibili_dinger.setIcon(FluentIcon.LINK)
        self.hyperlinkButton_bilibili_thun888.setIcon(FluentIcon.LINK)
