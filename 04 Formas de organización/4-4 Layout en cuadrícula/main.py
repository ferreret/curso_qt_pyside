from PySide6 import QtWidgets as qtw
import sys


class Caja(qtw.QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        cuadricula = qtw.QGridLayout()
        cuadricula.addWidget(Caja("orange"), 0, 0)
        cuadricula.addWidget(Caja("purple"), 1, 1)
        cuadricula.addWidget(Caja("magenta"), 2, 2)

        widget = qtw.QWidget()
        widget.setLayout(cuadricula)

        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
