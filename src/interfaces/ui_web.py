# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_web.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QWidget)

from qfluentwidgets import (ComboBox, LineEdit, PushButton)

class Ui_Web(object):
    def setupUi(self, Web):
        if not Web.objectName():
            Web.setObjectName(u"Web")
        Web.resize(800, 600)
        self.gridLayout_2 = QGridLayout(Web)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 509, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.PushButton_get_text = PushButton(Web)
        self.PushButton_get_text.setObjectName(u"PushButton_get_text")

        self.gridLayout_2.addWidget(self.PushButton_get_text, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.PushButton_choose_file = PushButton(Web)
        self.PushButton_choose_file.setObjectName(u"PushButton_choose_file")

        self.gridLayout.addWidget(self.PushButton_choose_file, 0, 2, 1, 1)

        self.LineEdit_url_or_html = LineEdit(Web)
        self.LineEdit_url_or_html.setObjectName(u"LineEdit_url_or_html")

        self.gridLayout.addWidget(self.LineEdit_url_or_html, 0, 1, 1, 1)

        self.ComboBox_where = ComboBox(Web)
        self.ComboBox_where.setObjectName(u"ComboBox_where")

        self.gridLayout.addWidget(self.ComboBox_where, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.PushButton_make_html = PushButton(Web)
        self.PushButton_make_html.setObjectName(u"PushButton_make_html")

        self.gridLayout_2.addWidget(self.PushButton_make_html, 2, 0, 1, 1)


        self.retranslateUi(Web)

        QMetaObject.connectSlotsByName(Web)
    # setupUi

    def retranslateUi(self, Web):
        Web.setWindowTitle(QCoreApplication.translate("Web", u"Form", None))
        self.PushButton_get_text.setText(QCoreApplication.translate("Web", u"\u63d0\u53d6\u6587\u672c", None))
        self.PushButton_choose_file.setText(QCoreApplication.translate("Web", u"\u6d4f\u89c8", None))
        self.PushButton_make_html.setText(QCoreApplication.translate("Web", u"\u751f\u6210\u7f51\u9875", None))
    # retranslateUi

