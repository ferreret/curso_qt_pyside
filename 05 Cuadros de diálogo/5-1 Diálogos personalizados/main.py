from PySide6 import QtWidgets as qtw
import sys


class Dialogo(qtw.QDialog):
    def __init__(self):
        super(Dialogo, self).__init__()
        self.setWindowTitle("Hola")
        self.resize(240, 120)

        layout = qtw.QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(qtw.QLabel("Diálogo de prueba"))
        botones = qtw.QDialogButtonBox(
            qtw.QDialogButtonBox.Ok | qtw.QDialogButtonBox.Cancel)

        botones.button(qtw.QDialogButtonBox.Ok).setText("Aceptar")
        botones.button(qtw.QDialogButtonBox.Cancel).setText("Cancelar")

        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)

        layout.addWidget(botones)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(480, 320)

        boton = qtw.QPushButton("Mostrar diálogo")
        boton.clicked.connect(self.boton_clicado)

        self.setCentralWidget(boton)

    def boton_clicado(self):
        dialogo = Dialogo()

        respuesta = dialogo.exec()

        if respuesta:
            print("Diálogo aceptado")
        else:
            print("Diálogo cancelado")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
