from PyQt6.QtWidgets import QMainWindow
from Window1Ext import WindowExt
from giaodien2 import Ui_MainWindow

class Window2Ext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_Continue.clicked.connect(self.processContinue)
    def showMainWindow(self):
        self.MainWindow.show()
    def processContinue(self):
        self.my_gui = WindowExt()
        self.my_gui.setupUi(QMainWindow())
        self.my_gui.showMainWindow()
        self.MainWindow.close()