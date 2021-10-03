from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
import sys
from pathlib import Path


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(qtc.QSize(480, 320))

        self.etiqueta = qtw.QLabel("Soy una etiqueta")
        # fuente = etiqueta.font()
        fuente = qtg.QFont()
        fuente.setFamily('Comic Sans MS')
        fuente.setPointSize(20)
        # fuente.setPointSize(24)
        self.etiqueta.setFont(fuente)
        self.etiqueta.setAlignment(qtc.Qt.AlignHCenter | qtc.Qt.AlignVCenter)

        imagen = qtg.QPixmap(absPath('naturaleza.jpg'))
        self.etiqueta.setPixmap(imagen)
        # hacemos que se escale con la ventana
        self.etiqueta.setScaledContents(True)

        self.setCentralWidget(self.etiqueta)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
