# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_settings.ui'
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

from qfluentwidgets import (CardWidget, CheckBox, ComboBox, LineEdit,
    SearchLineEdit, SmoothScrollArea, SpinBox, SubtitleLabel,
    TitleLabel)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(800, 600)
        self.gridLayout_10 = QGridLayout(Settings)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.SmoothScrollArea = SmoothScrollArea(Settings)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 780, 699))
        self.gridLayout_9 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.gridLayout_6 = QGridLayout(self.CardWidget_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.LineEdit_cookies = LineEdit(self.CardWidget_4)
        self.LineEdit_cookies.setObjectName(u"LineEdit_cookies")

        self.gridLayout_6.addWidget(self.LineEdit_cookies, 1, 0, 1, 1)

        self.TitleLabel_4 = TitleLabel(self.CardWidget_4)
        self.TitleLabel_4.setObjectName(u"TitleLabel_4")

        self.gridLayout_6.addWidget(self.TitleLabel_4, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.CardWidget_4, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 168, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.gridLayout_5 = QGridLayout(self.CardWidget_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.TitleLabel_3 = TitleLabel(self.CardWidget_3)
        self.TitleLabel_3.setObjectName(u"TitleLabel_3")

        self.gridLayout_5.addWidget(self.TitleLabel_3, 0, 0, 1, 1)

        self.SearchLineEdit_url_base = SearchLineEdit(self.CardWidget_3)
        self.SearchLineEdit_url_base.setObjectName(u"SearchLineEdit_url_base")

        self.gridLayout_5.addWidget(self.SearchLineEdit_url_base, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.CardWidget_3, 2, 0, 1, 1)

        self.CardWidget = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget.setObjectName(u"CardWidget")
        self.gridLayout_3 = QGridLayout(self.CardWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.TitleLabel = TitleLabel(self.CardWidget)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.gridLayout_3.addWidget(self.TitleLabel, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.CheckBox_proxies = CheckBox(self.CardWidget)
        self.CheckBox_proxies.setObjectName(u"CheckBox_proxies")

        self.gridLayout_2.addWidget(self.CheckBox_proxies, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.LineEdit_http = LineEdit(self.CardWidget)
        self.LineEdit_http.setObjectName(u"LineEdit_http")

        self.gridLayout.addWidget(self.LineEdit_http, 0, 1, 1, 1)

        self.LineEdit_https = LineEdit(self.CardWidget)
        self.LineEdit_https.setObjectName(u"LineEdit_https")

        self.gridLayout.addWidget(self.LineEdit_https, 1, 1, 1, 1)

        self.SubtitleLabel = SubtitleLabel(self.CardWidget)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.gridLayout.addWidget(self.SubtitleLabel, 0, 0, 1, 1)

        self.SubtitleLabel_2 = SubtitleLabel(self.CardWidget)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")

        self.gridLayout.addWidget(self.SubtitleLabel_2, 1, 0, 1, 1)

        self.SubtitleLabel_3 = SubtitleLabel(self.CardWidget)
        self.SubtitleLabel_3.setObjectName(u"SubtitleLabel_3")

        self.gridLayout.addWidget(self.SubtitleLabel_3, 2, 0, 1, 1)

        self.LineEdit_socks5 = LineEdit(self.CardWidget)
        self.LineEdit_socks5.setObjectName(u"LineEdit_socks5")

        self.gridLayout.addWidget(self.LineEdit_socks5, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.CardWidget, 0, 0, 1, 1)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        self.gridLayout_8 = QGridLayout(self.CardWidget_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.TitleLabel_5 = TitleLabel(self.CardWidget_5)
        self.TitleLabel_5.setObjectName(u"TitleLabel_5")

        self.gridLayout_8.addWidget(self.TitleLabel_5, 0, 0, 1, 2)

        self.SpinBox_max_thread_cnt = SpinBox(self.CardWidget_5)
        self.SpinBox_max_thread_cnt.setObjectName(u"SpinBox_max_thread_cnt")
        self.SpinBox_max_thread_cnt.setMinimum(1)
        self.SpinBox_max_thread_cnt.setMaximum(1000)
        self.SpinBox_max_thread_cnt.setValue(100)

        self.gridLayout_8.addWidget(self.SpinBox_max_thread_cnt, 1, 0, 1, 2)


        self.gridLayout_9.addWidget(self.CardWidget_5, 4, 0, 1, 1)

        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.gridLayout_4 = QGridLayout(self.CardWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.TitleLabel_2 = TitleLabel(self.CardWidget_2)
        self.TitleLabel_2.setObjectName(u"TitleLabel_2")

        self.gridLayout_4.addWidget(self.TitleLabel_2, 0, 0, 1, 1)

        self.ComboBox_lang = ComboBox(self.CardWidget_2)
        self.ComboBox_lang.setObjectName(u"ComboBox_lang")

        self.gridLayout_4.addWidget(self.ComboBox_lang, 1, 0, 1, 1)


        self.gridLayout_9.addWidget(self.CardWidget_2, 1, 0, 1, 1)

        self.CardWidget_6 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_6.setObjectName(u"CardWidget_6")
        self.gridLayout_7 = QGridLayout(self.CardWidget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.LineEdit_separator = LineEdit(self.CardWidget_6)
        self.LineEdit_separator.setObjectName(u"LineEdit_separator")

        self.gridLayout_7.addWidget(self.LineEdit_separator, 1, 0, 1, 1)

        self.TitleLabel_6 = TitleLabel(self.CardWidget_6)
        self.TitleLabel_6.setObjectName(u"TitleLabel_6")

        self.gridLayout_7.addWidget(self.TitleLabel_6, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.CardWidget_6, 5, 0, 1, 1)

        self.SmoothScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_10.addWidget(self.SmoothScrollArea, 0, 0, 1, 1)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Form", None))
        self.TitleLabel_4.setText(QCoreApplication.translate("Settings", u"\u81ea\u5b9a\u4e49cookies", None))
        self.TitleLabel_3.setText(QCoreApplication.translate("Settings", u"\u8c37\u6b4c\u7ffb\u8bd1\uff08\u955c\u50cf\uff09\u7f51\u7ad9\u8bbe\u7f6e", None))
        self.SearchLineEdit_url_base.setText(QCoreApplication.translate("Settings", u"https://gt.hzchu.top", None))
        self.TitleLabel.setText(QCoreApplication.translate("Settings", u"\u4ee3\u7406\u8bbe\u7f6e", None))
        self.CheckBox_proxies.setText(QCoreApplication.translate("Settings", u"\u4ee3\u7406", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Settings", u"http", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Settings", u"https", None))
        self.SubtitleLabel_3.setText(QCoreApplication.translate("Settings", u"socks5", None))
        self.TitleLabel_5.setText(QCoreApplication.translate("Settings", u"\u6700\u5927\u7ebf\u7a0b\u6570\u91cf", None))
        self.TitleLabel_2.setText(QCoreApplication.translate("Settings", u"\u8bed\u8a00\u8bbe\u7f6e", None))
        self.ComboBox_lang.setText("")
        self.LineEdit_separator.setText(QCoreApplication.translate("Settings", u"\\n\u3002\uff1f\uff01\uff1a,.", None))
        self.TitleLabel_6.setText(QCoreApplication.translate("Settings", u"\u5206\u9694\u7b26", None))
    # retranslateUi

