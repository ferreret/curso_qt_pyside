from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
import sys


class Caja(qtw.QLabel):
    def __init__(self, color):
        super(Caja, self).__init__()
        self.setStyleSheet(f"background-color: {color}")


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(qtc.QSize(480, 320))
        caja = Caja("green")
        self.setCentralWidget(caja)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
