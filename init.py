from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QGroupBox, QTextBrowser, QApplication
from PyQt5.QtCore import QSize, QRect, QCoreApplication, Qt
from PyQt5.QtGui import QFont
from sys import exit, argv
from time import sleep
from random import randint
from datetime import datetime

class Gui_Main(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.setFont(QFont("Microsoft YaHei UI"))
        self.resize(400, 215)
        self.setMinimumSize(QSize(400, 215))
        self.setMaximumSize(QSize(400, 215))
        self.Title = QLabel(self)
        self.Title.setGeometry(QRect(10, 10, 380, 15))
        self.Title.setStyleSheet(u"color: rgb(218, 114, 24);")
        self.BuleScreen = QPushButton(self)
        self.BuleScreen.setGeometry(QRect(15, 35, 100, 45))
        self.UEFI = QPushButton(self)
        self.UEFI.setGeometry(QRect(120, 35, 100, 45))
        self.BlueScreenCode = QLineEdit(self)
        self.BlueScreenCode.setGeometry(QRect(290, 36, 90, 20))
        self.BlueScreenCode.setEnabled(False)
        self.BlueScreenCode.setText("暂不支持")
        self.BlueScreenCodeTip = QLabel(self)
        self.BlueScreenCodeTip.setGeometry(QRect(225, 39, 60, 15))
        self.BIOSModeTip = QLabel(self)
        self.BIOSModeTip.setGeometry(QRect(225, 60, 60, 16))
        self.BIOSMode = QComboBox(self)
        self.BIOSMode.setGeometry(QRect(290, 58, 90, 20))
        self.BIOSMode.setEnabled(False)
        self.BIOSMode.addItem("自动检测")
        self.Log = QGroupBox(self)
        self.Log.setGeometry(QRect(15, 80, 370, 120))
        self.LogDisplay = QTextBrowser(self.Log)
        self.LogDisplay.setGeometry(QRect(5, 15, 360, 100))
        self.Tip = QLabel(self)
        self.Tip.setGeometry(QRect(1, 201, 265, 11))
        self.setWindowTitle(QCoreApplication.translate("Form", u"\u901a\u7528UEFI-CEF\u6ce8\u5165\u5668", None))
        self.Title.setText(QCoreApplication.translate("Form", u"\u8be5\u7a0b\u5e8f\u6b63\u5904\u4e8eDev\u5f00\u53d1\u7248\u4e2d\uff0c\u53ef\u80fd\u51fa\u73b0\u9519\u8bef\uff0c\u6ce8\u5165\u524d\u8bf7\u5907\u4efd\u7cfb\u7edf\u53ca\u6587\u4ef6\uff01", None))
        self.BuleScreen.setText(QCoreApplication.translate("Form", u"\u84dd\u5c4f\u6ce8\u5165", None))
        self.UEFI.setText(QCoreApplication.translate("Form", u"UEFI\u542f\u52a8\u6ce8\u5165", None))
        self.BlueScreenCodeTip.setText(QCoreApplication.translate("Form", u"\u84dd\u5c4f\u4ee3\u7801\uff1a", None))
        self.BIOSModeTip.setText(QCoreApplication.translate("Form", u"BIOS\u7c7b\u578b\uff1a", None))
        self.Log.setTitle(QCoreApplication.translate("Form", u"\u65e5\u5fd7\u8bb0\u5f55\u5668", None))
        self.Tip.setText(QCoreApplication.translate("Form", u"BIOS\u6a21\u5f0f(\u81ea\u52a8\u68c0\u6d4b)\uff1aUEFI BIOS  \u5b89\u5168\u6a21\u5f0f\uff1a\u5426", None))
        
    def down(self):
        self.LogDisplay.append(Functions.GetLogTimeDisplay()+"加载完毕！")

class Gui_Setup(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.resize(395, 90)
        self.setMinimumSize(QSize(395, 90))
        self.setMaximumSize(QSize(395, 90))
        self.setWindowTitle(QCoreApplication.translate("Form", u"\u901a\u7528UEFI-CEF\u6ce8\u5165\u5668", None))
        self.setFont(QFont("Microsoft YaHei UI", 20))
        self.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
                            "color: rgb(255, 255, 255);")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 30, 250, 30))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText(QCoreApplication.translate("Form", u"\u52a0\u8f7d\u6587\u4ef6...", None))
        self.show()
        self.setup()
        
    def setup(self):
        self.label.setText("检测BIOS引导模式...")
        QApplication.processEvents()
        sleep(randint(100, 200)/100)
        self.label.setText("加载控件...")
        QApplication.processEvents()
        sleep(randint(100, 200)/100)
        self.label.setText("加载文件...")
        QApplication.processEvents()
        sleep(randint(100, 200)/100)
        self.close()
        window1.show()
        window1.down()
        
class Functions():
    def GetLogTimeDisplay() -> str:
        return str("["+str(datetime.now())+"] ")

app1 = QApplication(argv)
app2 = QApplication(argv)
window1 = Gui_Main()
window2 = Gui_Setup()
exit(app1.exec_())