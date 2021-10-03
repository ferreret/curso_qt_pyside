from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
import sys


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setMinimumSize(qtc.QSize(480, 320))

        casilla = qtw.QCheckBox("Casilla de verificación")
        casilla.stateChanged.connect(self.estado_cambiado)
        self.setCentralWidget(casilla)

    def estado_cambiado(self, estado):
        if estado == qtc.Qt.Checked:
            print("Casilla Marcada")
        else:
            print("Casilla desmarcada")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
