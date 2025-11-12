from PyQt6.QtWidgets import QApplication, QMainWindow

from WindowExt import WindowExt

app=QApplication([])
myWindow=(WindowExt())
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()