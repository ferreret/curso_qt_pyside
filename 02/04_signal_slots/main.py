from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hola mundo')
        self.boton = QPushButton('Soy un botón')
        self.boton.setCheckable(True)
        self.setCentralWidget(self.boton)

        self.setMinimumSize(QSize(480, 320))
        self.setMaximumSize(QSize(800, 600))

        # boton.clicked.connect(self.boton_clicado)
        self.boton.clicked.connect(self.boton_alternado)

    # def boton_clicado(self):
    #     print('Botón clicado')

    def boton_alternado(self, valor):
        if valor:
            self.boton.setText('Estoy activado')
        else:
            self.boton.setText('Estoy desactivado')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
