# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 215)
        Form.setMinimumSize(QSize(400, 215))
        Form.setMaximumSize(QSize(400, 215))
        self.Title = QLabel(Form)
        self.Title.setObjectName(u"Title")
        self.Title.setGeometry(QRect(10, 10, 380, 15))
        self.Title.setStyleSheet(u"color: rgb(218, 114, 24);")
        self.BuleScreen = QPushButton(Form)
        self.BuleScreen.setObjectName(u"BuleScreen")
        self.BuleScreen.setGeometry(QRect(15, 35, 100, 45))
        self.UEFI = QPushButton(Form)
        self.UEFI.setObjectName(u"UEFI")
        self.UEFI.setGeometry(QRect(120, 35, 100, 45))
        self.BlueScreenCode = QLineEdit(Form)
        self.BlueScreenCode.setObjectName(u"BlueScreenCode")
        self.BlueScreenCode.setGeometry(QRect(290, 36, 90, 20))
        self.BlueScreenCodeTip = QLabel(Form)
        self.BlueScreenCodeTip.setObjectName(u"BlueScreenCodeTip")
        self.BlueScreenCodeTip.setGeometry(QRect(225, 39, 60, 15))
        self.BlueScreenCodeTip.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.BIOSModeTip = QLabel(Form)
        self.BIOSModeTip.setObjectName(u"BIOSModeTip")
        self.BIOSModeTip.setGeometry(QRect(225, 60, 60, 16))
        self.BIOSMode = QComboBox(Form)
        self.BIOSMode.setObjectName(u"BIOSMode")
        self.BIOSMode.setGeometry(QRect(290, 58, 90, 20))
        self.Log = QGroupBox(Form)
        self.Log.setObjectName(u"Log")
        self.Log.setGeometry(QRect(15, 80, 370, 120))
        self.LogDisplay = QTextBrowser(self.Log)
        self.LogDisplay.setObjectName(u"LogDisplay")
        self.LogDisplay.setGeometry(QRect(5, 15, 360, 100))
        self.Tip = QLabel(Form)
        self.Tip.setObjectName(u"Tip")
        self.Tip.setGeometry(QRect(1, 201, 265, 11))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u901a\u7528UEFI-CEF\u6ce8\u5165\u5668", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u8be5\u7a0b\u5e8f\u6b63\u5904\u4e8eDev\u5f00\u53d1\u7248\u4e2d\uff0c\u53ef\u80fd\u51fa\u73b0\u9519\u8bef\uff0c\u6ce8\u5165\u524d\u8bf7\u5907\u4efd\u7cfb\u7edf\u53ca\u6587\u4ef6\uff01", None))
        self.BuleScreen.setText(QCoreApplication.translate("Form", u"\u84dd\u5c4f\u6ce8\u5165", None))
        self.UEFI.setText(QCoreApplication.translate("Form", u"UEFI\u542f\u52a8\u6ce8\u5165", None))
        self.BlueScreenCodeTip.setText(QCoreApplication.translate("Form", u"\u84dd\u5c4f\u4ee3\u7801\uff1a", None))
        self.BIOSModeTip.setText(QCoreApplication.translate("Form", u"BIOS\u7c7b\u578b\uff1a", None))
        self.Log.setTitle(QCoreApplication.translate("Form", u"\u65e5\u5fd7\u8bb0\u5f55\u5668", None))
        self.Tip.setText(QCoreApplication.translate("Form", u"BIOS\u6a21\u5f0f(\u81ea\u52a8\u68c0\u6d4b)\uff1aUEFI BIOS  \u5b89\u5168\u6a21\u5f0f\uff1a\u5426", None))
    # retranslateUi

