from PyQt6.QtWidgets import QMainWindow, QMessageBox
from giaodien1 import Ui_MainWindow


class WindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.pushButton_payment.clicked.connect(self.processPayment)
        self.lineEdit_cream.textChanged.connect(self.total_value)
        self.lineEdit_showergel.textChanged.connect(self.total_value)
        self.lineEdit_bdywash.textChanged.connect(self.total_value)
        self.lineEdit_cleanser.textChanged.connect(self.total_value)
        self.lineEdit_moisturiser.textChanged.connect(self.total_value)
        self.Phanthuong.clicked.connect(self.Reward)
    def showMainWindow(self):
        self.MainWindow.show()
    def processPayment(self):
        msg = QMessageBox()
        msg.setWindowTitle("Xác nhận thanh toán")
        msg.setText("Xác nhận đơn hàng?")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.Ok:
            self.MainWindow.close()
    def total_value(self):
        pass
    def Reward(self):
        pass




