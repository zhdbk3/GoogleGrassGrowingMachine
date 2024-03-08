from PySide6.QtWidgets import QWidget

from .ui_web import Ui_Web

if __name__ == '__main__':
    from main import Window


class InterfaceWeb(QWidget, Ui_Web):
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
        self.ComboBox_where.addItems(['URL', 'HTML'])
