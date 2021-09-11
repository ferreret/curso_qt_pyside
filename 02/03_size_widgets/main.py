from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hola mundo')
        boton = QPushButton('Soy un botón')
        self.setCentralWidget(boton)

        self.setMinimumSize(QSize(480, 320))
        self.setMaximumSize(QSize(800, 600))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
