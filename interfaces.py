from PyQt5.QtWidgets import QWidget

from ui_files import ui_translate, ui_web, ui_doc, ui_settings, ui_about


class InterfaceTranslate(QWidget, ui_translate.Ui_Form):
    """导入生草页面"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('InterfaceTranslate')

    # def addSubInterface(self, interface: QWidget, icon: Union[FluentIconBase, QIcon, str], text: str,
    #                         position=NavigationItemPosition.TOP, parent=None) -> NavigationTreeWidget:


class InterfaceWeb(QWidget, ui_web.Ui_Form):
    """导入网页生草页面"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('InterfaceWeb')


class InterfaceDoc(QWidget, ui_doc.Ui_Form):
    """导入文档生草页面"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('InterfaceDoc')


class InterfaceSettings(QWidget, ui_settings.Ui_Form):
    """导入设置页面"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('InterfaceSettings')


class InterfaceAbout(QWidget, ui_about.Ui_Form):
    """导入关于页面"""

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        # 必须给子界面设置全局唯一的对象名
        self.setObjectName('InterfaceAbout')
