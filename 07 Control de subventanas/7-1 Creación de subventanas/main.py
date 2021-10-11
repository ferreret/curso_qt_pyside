import sys

from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
                               QVBoxLayout, QWidget)


class Subventana(QWidget):
    def __init__(self):
        super(Subventana, self).__init__()
        self.resize(240, 120)
        self.setWindowTitle("Subventana")
        etiqueta = QLabel("Soy una subventana")
        layout = QVBoxLayout()
        layout.addWidget(etiqueta)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Le damos tamaño y título
        self.setWindowTitle("Ventana principal")
        self.resize(480, 320)
        # Dummy widget para layout
        layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # Botón para abrir la subventana
        boton_mostrar = QPushButton("Mostrar subventana")
        boton_mostrar.clicked.connect(self.mostrar_subventana)
        layout.addWidget(boton_mostrar)

        boton_ocultar = QPushButton("Ocultar subventana")
        boton_ocultar.clicked.connect(self.ocultar_subventana)
        layout.addWidget(boton_ocultar)

        self.subventana = Subventana()

    def ocultar_subventana(self):
        if Wself.subventana.isVisible():
            self.subventana.close()

    def mostrar_subventana(self):
        if not self.subventana:
            self.subventana = Subventana()
        self.subventana.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
