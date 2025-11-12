from PyQt6.QtWidgets import QMessageBox

from giaodien2 import Ui_MainWindow

class Window2Ext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_payment.clicked.connect(self.processPayment)
    def show(self):
        self.MainWindow.show()
    def processPayment(self):
        msg=QMessageBox()


