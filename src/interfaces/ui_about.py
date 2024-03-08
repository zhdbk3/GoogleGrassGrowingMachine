# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_about.ui'
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

from qfluentwidgets import (AvatarWidget, BodyLabel, CardWidget, ElevatedCardWidget,
    HyperlinkButton, ImageLabel, PushButton, SimpleCardWidget,
    StrongBodyLabel)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(800, 600)
        self.gridLayout_8 = QGridLayout(About)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer, 4, 0, 1, 2)

        self.ElevatedCardWidget_supporters = ElevatedCardWidget(About)
        self.ElevatedCardWidget_supporters.setObjectName(u"ElevatedCardWidget_supporters")
        self.gridLayout_7 = QGridLayout(self.ElevatedCardWidget_supporters)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.HyperlinkButton_thun888 = HyperlinkButton(self.ElevatedCardWidget_supporters)
        self.HyperlinkButton_thun888.setObjectName(u"HyperlinkButton_thun888")
        self.HyperlinkButton_thun888.setUrl(QUrl(u"https://space.bilibili.com/451090261"))
        self.HyperlinkButton_thun888.setProperty("hasIcon", True)

        self.gridLayout_3.addWidget(self.HyperlinkButton_thun888, 0, 5, 1, 1)

        self.HyperlinkButton_statistics = HyperlinkButton(self.ElevatedCardWidget_supporters)
        self.HyperlinkButton_statistics.setObjectName(u"HyperlinkButton_statistics")
        self.HyperlinkButton_statistics.setUrl(QUrl(u"http://gt-stats.757678.xyz/"))
        self.HyperlinkButton_statistics.setProperty("hasIcon", True)

        self.gridLayout_3.addWidget(self.HyperlinkButton_statistics, 0, 4, 1, 1)

        self.BodyLabel_3 = BodyLabel(self.ElevatedCardWidget_supporters)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")

        self.gridLayout_3.addWidget(self.BodyLabel_3, 0, 1, 1, 1)

        self.AvatarWidget_thun888 = AvatarWidget(self.ElevatedCardWidget_supporters)
        self.AvatarWidget_thun888.setObjectName(u"AvatarWidget_thun888")
        self.AvatarWidget_thun888.setRadius(20)

        self.gridLayout_3.addWidget(self.AvatarWidget_thun888, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.BodyLabel_4 = BodyLabel(self.ElevatedCardWidget_supporters)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        self.BodyLabel_4.setProperty("lightColor", QColor(128, 128, 128))

        self.gridLayout_3.addWidget(self.BodyLabel_4, 0, 2, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 1, 0, 1, 1)

        self.StrongBodyLabel_2 = StrongBodyLabel(self.ElevatedCardWidget_supporters)
        self.StrongBodyLabel_2.setObjectName(u"StrongBodyLabel_2")

        self.gridLayout_7.addWidget(self.StrongBodyLabel_2, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.ElevatedCardWidget_supporters, 3, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_2, 1, 0, 1, 2)

        self.ElevatedCardWidget = ElevatedCardWidget(About)
        self.ElevatedCardWidget.setObjectName(u"ElevatedCardWidget")
        self.gridLayout_5 = QGridLayout(self.ElevatedCardWidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.HyperlinkButton_xdedan = HyperlinkButton(self.ElevatedCardWidget)
        self.HyperlinkButton_xdedan.setObjectName(u"HyperlinkButton_xdedan")
        self.HyperlinkButton_xdedan.setUrl(QUrl(u"https://space.bilibili.com/668182235"))
        self.HyperlinkButton_xdedan.setProperty("hasIcon", True)

        self.gridLayout_2.addWidget(self.HyperlinkButton_xdedan, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.AvatarWidget_xdedan = AvatarWidget(self.ElevatedCardWidget)
        self.AvatarWidget_xdedan.setObjectName(u"AvatarWidget_xdedan")
        self.AvatarWidget_xdedan.setRadius(20)

        self.gridLayout_2.addWidget(self.AvatarWidget_xdedan, 0, 0, 1, 1)

        self.BodyLabel_2 = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")

        self.gridLayout_2.addWidget(self.BodyLabel_2, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.HyperlinkButton_mczhdbk = HyperlinkButton(self.ElevatedCardWidget)
        self.HyperlinkButton_mczhdbk.setObjectName(u"HyperlinkButton_mczhdbk")
        self.HyperlinkButton_mczhdbk.setUrl(QUrl(u"https://space.bilibili.com/551409211"))
        self.HyperlinkButton_mczhdbk.setProperty("hasIcon", True)

        self.gridLayout.addWidget(self.HyperlinkButton_mczhdbk, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.AvatarWidget_mczhdbk = AvatarWidget(self.ElevatedCardWidget)
        self.AvatarWidget_mczhdbk.setObjectName(u"AvatarWidget_mczhdbk")
        self.AvatarWidget_mczhdbk.setRadius(20)

        self.gridLayout.addWidget(self.AvatarWidget_mczhdbk, 0, 0, 1, 1)

        self.BodyLabel = BodyLabel(self.ElevatedCardWidget)
        self.BodyLabel.setObjectName(u"BodyLabel")

        self.gridLayout.addWidget(self.BodyLabel, 0, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.StrongBodyLabel = StrongBodyLabel(self.ElevatedCardWidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")

        self.gridLayout_5.addWidget(self.StrongBodyLabel, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.ElevatedCardWidget, 0, 0, 1, 2)

        self.HyperlinkButton_github = HyperlinkButton(About)
        self.HyperlinkButton_github.setObjectName(u"HyperlinkButton_github")
        self.HyperlinkButton_github.setUrl(QUrl(u"https://github.com/zhdbk3/GoogleGrassGrowingMachine"))
        self.HyperlinkButton_github.setProperty("hasIcon", True)

        self.gridLayout_8.addWidget(self.HyperlinkButton_github, 5, 0, 1, 2)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"Form", None))
        self.HyperlinkButton_thun888.setText(QCoreApplication.translate("About", u"bilibili", None))
        self.HyperlinkButton_statistics.setText(QCoreApplication.translate("About", u"\u4f7f\u7528\u7edf\u8ba1", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("About", u"thun888", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("About", u"\u63d0\u4f9b\u955c\u50cf\u7f51\u7ad9", None))
        self.StrongBodyLabel_2.setText(QCoreApplication.translate("About", u"\u652f\u6301\u8005", None))
        self.HyperlinkButton_xdedan.setText(QCoreApplication.translate("About", u"bilibili", None))
        self.AvatarWidget_xdedan.setText("")
        self.BodyLabel_2.setText(QCoreApplication.translate("About", u"\u859b\u5b9a\u8c14\u7684\u6309\u94ae", None))
        self.HyperlinkButton_mczhdbk.setText(QCoreApplication.translate("About", u"bilibili", None))
        self.BodyLabel.setText(QCoreApplication.translate("About", u"MC\u7740\u706b\u7684\u51b0\u5757", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("About", u"\u8c37\u6b4c\u751f\u8349\u673a\u5f00\u53d1\u8005", None))
        self.HyperlinkButton_github.setText(QCoreApplication.translate("About", u"github\u4ed3\u5e93", None))
    # retranslateUi

