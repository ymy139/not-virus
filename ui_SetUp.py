# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetUp.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(395, 90)
        Form.setMinimumSize(QSize(395, 90))
        Form.setMaximumSize(QSize(395, 90))
        font = QFont()
        font.setPointSize(20)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 250, 30))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u901a\u7528UEFI-CEF\u6ce8\u5165\u5668", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u52a0\u8f7d\u6587\u4ef6...", None))
    # retranslateUi

