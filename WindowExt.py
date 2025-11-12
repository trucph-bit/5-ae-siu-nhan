from PyQt6.QtWidgets import QMainWindow

from Window2Ext import Window2Ext
from giaodien1 import Ui_MainWindow


class WindowExt(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.continue_2.clicked.connect(self.processContinue)
    def show(self):
        self.MainWindow.show()
    def processContinue(self):
        self.my_gui = Window2Ext()
        self.my_gui.setupUi(QMainWindow())
        self.MainWindow.close()
        qcleanser=int(self.lineEdit_cleanser.text())
        qbodywash=int(self.lineEdit_bdywash.text())
        qmoisturizer=int(self.lineEdit_moisturiser.text())
        qgel=int(self.lineEdit_showergel.text())
        qcream=int(self.lineEdit_cream.text())
        vcleanser=98.500*qcleanser
        vbodywash=275.600*qbodywash
        vmoisturizer=180.000*qmoisturizer
        vcream=190.600*qcream
        vgel=254.300*qgel
        total= vcleanser+vbodywash+vmoisturizer+vcream+vgel
        self.lineEdit_cleanser.setText(str(total))

