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
        quantity_moisturiser = int(self.lineEdit_moisturiser.text())
        quantity_bdywash = int(self.lineEdit_bdywash.text())
        quantity_cleanser = int(self.lineEdit_cleanser.text())
        quantity_showergel = int(self.lineEdit_showergel.text())
        quantity_cream = int(self.lineEdit_cream.text())
        total_value_calculated = (quantity_moisturiser * 180000) + \
                                 (quantity_bdywash * 275600) + \
                                 (quantity_cleanser * 98500) + \
                                 (quantity_showergel * 254300) + \
                                 (quantity_cream * 190600)
        return total_value_calculated
    def Reward(self):
        total_value_calculated=self.total_value()
        self.Phanthuong.hide()
        if total_value_calculated >= 1000000:
            self.label_26.setText("Xin chúc mừng! Bạn đã nhận được bộ serum dưỡng ẩm trị giá 300k")
            elif total_value_calculated >= 500000:
                self.label_26.setText("Xin chúc mừng! Bạn đã nhận được set mặt nạ trị giá 119k")
            elif total_value_calculated >= 100000:
                self.label_26.setText("Xin chúc mừng! Bạn đã nhận được bông tẩy trang trị giá 39k"))




