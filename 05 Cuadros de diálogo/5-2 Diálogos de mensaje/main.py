from PySide6 import QtWidgets as qtw
import sys


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(480, 320)

        boton = qtw.QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = qtw.QMessageBox(self)
        dialogo.setWindowTitle("Título de ejemplo")
        dialogo.setText("Esto es un diálogo de prueba")

        dialogo.setStandardButtons(qtw.QMessageBox.Ok | qtw.QMessageBox.Cancel)
        dialogo.setIcon(qtw.QMessageBox.Question)
        respuesta = dialogo.exec()
        if respuesta == qtw.QMessageBox.Ok:
            print("Aceptado")
        else:
            print("Cancelado")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
