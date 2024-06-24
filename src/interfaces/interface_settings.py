from PyQt5.QtWidgets import QWidget
from qfluentwidgets import FlowLayout, CheckBox
from aiogoogletrans import LANGCODES

from .ui_settings import Ui_FormSettings


class InterfaceSettings(QWidget, Ui_FormSettings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 存放语言勾选项的流式布局
        self.flowLayout_lang = FlowLayout(needAni=True)
        # 存放所有语言勾选项的列表
        self.checkBoxes_lang: list[CheckBox] = []

        self.init_ui()

    def init_ui(self):
        # 将流式布局添加进卡片
        self.gridLayout_lang.addLayout(self.flowLayout_lang, 1, 0, 1, 1)
        # 添加按钮
        for lang in LANGCODES.keys():
            checkBox = CheckBox(lang)
            checkBox.setChecked(True)
            self.checkBoxes_lang.append(checkBox)
            self.flowLayout_lang.addWidget(checkBox)

    @property
    def selected_langs(self) -> list[str]:
        return [LANGCODES[cb.text()] for cb in self.checkBoxes_lang if cb.isChecked()]
