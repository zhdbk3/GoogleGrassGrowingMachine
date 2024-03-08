# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_translate.ui'
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

from qfluentwidgets import (ImageLabel, PlainTextEdit, PrimaryPushButton, ProgressBar,
    PushButton, RadioButton, SpinBox, SubtitleLabel,
    TitleLabel, TransparentPushButton)

class Ui_Translate(object):
    def setupUi(self, Translate):
        if not Translate.objectName():
            Translate.setObjectName(u"Translate")
        Translate.resize(800, 600)
        self.gridLayout_9 = QGridLayout(Translate)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.PlainTextEdit_output = PlainTextEdit(Translate)
        self.PlainTextEdit_output.setObjectName(u"PlainTextEdit_output")
        self.PlainTextEdit_output.setReadOnly(True)

        self.gridLayout_9.addWidget(self.PlainTextEdit_output, 4, 0, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.PushButton_ctrl_c = PushButton(Translate)
        self.PushButton_ctrl_c.setObjectName(u"PushButton_ctrl_c")
        self.PushButton_ctrl_c.setProperty("hasIcon", True)

        self.gridLayout_8.addWidget(self.PushButton_ctrl_c, 0, 0, 1, 1)

        self.PushButton_download_mp3 = PushButton(Translate)
        self.PushButton_download_mp3.setObjectName(u"PushButton_download_mp3")
        self.PushButton_download_mp3.setProperty("hasIcon", True)

        self.gridLayout_8.addWidget(self.PushButton_download_mp3, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_8, 5, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.TitleLabel = TitleLabel(Translate)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.gridLayout.addWidget(self.TitleLabel, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.PushButton_ctrl_v = PushButton(Translate)
        self.PushButton_ctrl_v.setObjectName(u"PushButton_ctrl_v")
        self.PushButton_ctrl_v.setProperty("hasIcon", True)

        self.gridLayout.addWidget(self.PushButton_ctrl_v, 0, 2, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.PlainTextEdit_input = PlainTextEdit(Translate)
        self.PlainTextEdit_input.setObjectName(u"PlainTextEdit_input")

        self.gridLayout_9.addWidget(self.PlainTextEdit_input, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.SpinBox_timeout = SpinBox(Translate)
        self.SpinBox_timeout.setObjectName(u"SpinBox_timeout")
        self.SpinBox_timeout.setValue(5)

        self.gridLayout_2.addWidget(self.SpinBox_timeout, 0, 3, 1, 1)

        self.SubtitleLabel_2 = SubtitleLabel(Translate)
        self.SubtitleLabel_2.setObjectName(u"SubtitleLabel_2")

        self.gridLayout_2.addWidget(self.SubtitleLabel_2, 0, 2, 1, 1)

        self.SpinBox_times = SpinBox(Translate)
        self.SpinBox_times.setObjectName(u"SpinBox_times")

        self.gridLayout_2.addWidget(self.SpinBox_times, 0, 1, 1, 1)

        self.SubtitleLabel = SubtitleLabel(Translate)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.gridLayout_2.addWidget(self.SubtitleLabel, 0, 0, 1, 1)

        self.SubtitleLabel_4 = SubtitleLabel(Translate)
        self.SubtitleLabel_4.setObjectName(u"SubtitleLabel_4")

        self.gridLayout_2.addWidget(self.SubtitleLabel_4, 0, 4, 1, 1)

        self.SpinBox_retry = SpinBox(Translate)
        self.SpinBox_retry.setObjectName(u"SpinBox_retry")
        self.SpinBox_retry.setValue(5)

        self.gridLayout_2.addWidget(self.SpinBox_retry, 0, 5, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.RadioButton_together = RadioButton(Translate)
        self.RadioButton_together.setObjectName(u"RadioButton_together")
        self.RadioButton_together.setChecked(True)

        self.gridLayout_3.addWidget(self.RadioButton_together, 0, 0, 1, 1)

        self.RadioButton_sentences = RadioButton(Translate)
        self.RadioButton_sentences.setObjectName(u"RadioButton_sentences")

        self.gridLayout_3.addWidget(self.RadioButton_sentences, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.PrimaryPushButton_start = PrimaryPushButton(Translate)
        self.PrimaryPushButton_start.setObjectName(u"PrimaryPushButton_start")
        self.PrimaryPushButton_start.setProperty("hasIcon", True)

        self.gridLayout_5.addWidget(self.PrimaryPushButton_start, 0, 2, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_5, 2, 0, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.TitleLabel_4 = TitleLabel(Translate)
        self.TitleLabel_4.setObjectName(u"TitleLabel_4")

        self.gridLayout_6.addWidget(self.TitleLabel_4, 0, 1, 1, 1)

        self.ProgressBar = ProgressBar(Translate)
        self.ProgressBar.setObjectName(u"ProgressBar")
        font = QFont()
        font.setPointSize(9)
        font.setBold(False)
        self.ProgressBar.setFont(font)

        self.gridLayout_6.addWidget(self.ProgressBar, 0, 2, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.SubtitleLabel_timer = SubtitleLabel(Translate)
        self.SubtitleLabel_timer.setObjectName(u"SubtitleLabel_timer")

        self.gridLayout_7.addWidget(self.SubtitleLabel_timer, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.TransparentPushButton_info = TransparentPushButton(Translate)
        self.TransparentPushButton_info.setObjectName(u"TransparentPushButton_info")

        self.gridLayout_7.addWidget(self.TransparentPushButton_info, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_7, 1, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.ImageLabel = ImageLabel(Translate)
        self.ImageLabel.setObjectName(u"ImageLabel")

        self.gridLayout_11.addWidget(self.ImageLabel, 0, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_11, 3, 0, 1, 1)


        self.retranslateUi(Translate)

        QMetaObject.connectSlotsByName(Translate)
    # setupUi

    def retranslateUi(self, Translate):
        Translate.setWindowTitle(QCoreApplication.translate("Translate", u"Form", None))
        self.PushButton_ctrl_c.setText(QCoreApplication.translate("Translate", u"\u4e00\u952e\u590d\u5236", None))
        self.PushButton_download_mp3.setText(QCoreApplication.translate("Translate", u"\u4e0b\u8f7d\u97f3\u9891", None))
        self.TitleLabel.setText(QCoreApplication.translate("Translate", u"\u8bf7\u8f93\u5165\u8981\u751f\u8349\u7684\u5185\u5bb9\uff1a", None))
        self.PushButton_ctrl_v.setText(QCoreApplication.translate("Translate", u"\u4e00\u952e\u7c98\u8d34", None))
        self.SubtitleLabel_2.setText(QCoreApplication.translate("Translate", u"\u8d85\u65f6\uff1a", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("Translate", u"\u7ffb\u8bd1\u6b21\u6570\uff1a", None))
        self.SubtitleLabel_4.setText(QCoreApplication.translate("Translate", u"\u91cd\u8bd5\u6b21\u6570\uff1a", None))
        self.RadioButton_together.setText(QCoreApplication.translate("Translate", u"\u6574\u4f53\u7ffb\u8bd1", None))
        self.RadioButton_sentences.setText(QCoreApplication.translate("Translate", u"\u9010\u53e5\u7ffb\u8bd1", None))
        self.PrimaryPushButton_start.setText(QCoreApplication.translate("Translate", u"\u5f00\u59cb\u7ffb\u8bd1", None))
        self.TitleLabel_4.setText(QCoreApplication.translate("Translate", u"\u751f\u8349\u7ed3\u679c\uff1a", None))
        self.SubtitleLabel_timer.setText(QCoreApplication.translate("Translate", u"\u7528\u65f6 00:00:00.00", None))
        self.TransparentPushButton_info.setText(QCoreApplication.translate("Translate", u"\u672a\u7ffb\u8bd1", None))
    # retranslateUi

