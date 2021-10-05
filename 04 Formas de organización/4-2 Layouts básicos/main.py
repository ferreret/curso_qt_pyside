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

        layout = qtw.QHBoxLayout()
        layout.addWidget(Caja("green"))
        layout.addWidget(Caja("blue"))
        layout.addWidget(Caja("red"))
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        widget = qtw.QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
