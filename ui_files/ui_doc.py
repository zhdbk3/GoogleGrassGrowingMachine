# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_doc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.PushButton_make_doc = PushButton(Form)
        self.PushButton_make_doc.setObjectName("PushButton_make_doc")
        self.gridLayout_2.addWidget(self.PushButton_make_doc, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(779, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.PushButton_go = PushButton(Form)
        self.PushButton_go.setObjectName("PushButton_go")
        self.gridLayout_2.addWidget(self.PushButton_go, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 509, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 7, 0, 1, 1)
        self.PushButton_get_text = PushButton(Form)
        self.PushButton_get_text.setObjectName("PushButton_get_text")
        self.gridLayout_2.addWidget(self.PushButton_get_text, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.PushButton_choose_file = PushButton(Form)
        self.PushButton_choose_file.setObjectName("PushButton_choose_file")
        self.gridLayout.addWidget(self.PushButton_choose_file, 0, 2, 1, 1)
        self.LineEdit_doc = LineEdit(Form)
        self.LineEdit_doc.setObjectName("LineEdit_doc")
        self.gridLayout.addWidget(self.LineEdit_doc, 0, 1, 1, 1)
        self.ComboBox_where = ComboBox(Form)
        self.ComboBox_where.setObjectName("ComboBox_where")
        self.gridLayout.addWidget(self.ComboBox_where, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.PushButton_make_doc.setText(_translate("Form", "合成文件"))
        self.PushButton_go.setText(_translate("Form", "开始生草（详细设置请到首页）"))
        self.PushButton_get_text.setText(_translate("Form", "读取文件"))
        self.PushButton_choose_file.setText(_translate("Form", "浏览"))
from qfluentwidgets import ComboBox, LineEdit, PushButton
