from PyQt6.QtWidgets import QApplication, QMainWindow
from Window2Ext import Window2Ext

app=QApplication([])
myWindow=(Window2Ext())
myWindow.setupUi(QMainWindow())
myWindow.showMainWindow()
app.exec()