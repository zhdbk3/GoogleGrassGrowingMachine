# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.gridLayout_6 = QtWidgets.QGridLayout(Form)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.TitleLabel = TitleLabel(Form)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout_3.addWidget(self.TitleLabel, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CheckBox_proxies = CheckBox(Form)
        self.CheckBox_proxies.setObjectName("CheckBox_proxies")
        self.gridLayout_2.addWidget(self.CheckBox_proxies, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.LineEdit_http = LineEdit(Form)
        self.LineEdit_http.setObjectName("LineEdit_http")
        self.gridLayout.addWidget(self.LineEdit_http, 0, 1, 1, 1)
        self.SubtitleLabel_2 = SubtitleLabel(Form)
        self.SubtitleLabel_2.setObjectName("SubtitleLabel_2")
        self.gridLayout.addWidget(self.SubtitleLabel_2, 1, 0, 1, 1)
        self.LineEdit_https = LineEdit(Form)
        self.LineEdit_https.setObjectName("LineEdit_https")
        self.gridLayout.addWidget(self.LineEdit_https, 1, 1, 1, 1)
        self.SubtitleLabel = SubtitleLabel(Form)
        self.SubtitleLabel.setObjectName("SubtitleLabel")
        self.gridLayout.addWidget(self.SubtitleLabel, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 2, 0, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(657, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 0, 1, 2)
        self.TitleLabel_2 = TitleLabel(Form)
        self.TitleLabel_2.setObjectName("TitleLabel_2")
        self.gridLayout_4.addWidget(self.TitleLabel_2, 1, 0, 1, 2)
        self.ComboBox_lang = ComboBox(Form)
        self.ComboBox_lang.setText("")
        self.ComboBox_lang.setObjectName("ComboBox_lang")
        self.gridLayout_4.addWidget(self.ComboBox_lang, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_4, 3, 0, 1, 2)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem4, 0, 0, 1, 1)
        self.TitleLabel_3 = TitleLabel(Form)
        self.TitleLabel_3.setObjectName("TitleLabel_3")
        self.gridLayout_5.addWidget(self.TitleLabel_3, 1, 0, 1, 1)
        self.LineEdit_cookies = LineEdit(Form)
        self.LineEdit_cookies.setText("")
        self.LineEdit_cookies.setObjectName("LineEdit_cookies")
        self.gridLayout_5.addWidget(self.LineEdit_cookies, 2, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 4, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem5, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TitleLabel.setText(_translate("Form", "代理设置"))
        self.CheckBox_proxies.setText(_translate("Form", "代理"))
        self.SubtitleLabel_2.setText(_translate("Form", "https"))
        self.SubtitleLabel.setText(_translate("Form", "http"))
        self.TitleLabel_2.setText(_translate("Form", "语言设置"))
        self.TitleLabel_3.setText(_translate("Form", "自定义cookies"))
from qfluentwidgets import CheckBox, ComboBox, LineEdit, SubtitleLabel, TitleLabel