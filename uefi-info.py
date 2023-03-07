from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from PyQt5.QtCore import QSize, QRect, QCoreApplication, Qt, QPoint
from PyQt5.QtGui import QFont
from sys import argv, exit

class window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setupUI()
        
    def setupUI(self):
        self.setStyleSheet("background-color: rgb(0, 0, 0);\ncolor: rgb(255, 255, 255);")
        #self.setWindowFlag()
        self.resize(QSize(1920, 1040))
        self.move(QPoint(0, 0))
        self.setFont(QFont("Microsoft YaHei UI", 10))
        
        self.lbl = QLabel(self)
        self.lbl.setFont(QFont("Microsoft YaHei UI", 10))
        self.lbl.resize(QSize(1920, 1040))
        self.lbl.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lbl.setText("test\ntest")
        
        self.show()
        
app = QApplication(argv)
windowfrom = window()
exit(app.exec_())