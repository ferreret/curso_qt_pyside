from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('Hola mundo')
button = QPushButton('Soy un botón')
window.setCentralWidget(button)

window.show()

sys.exit(app.exec())
