import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
from helpers import absPath
from ui_tabla import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        connection = QSqlDatabase.addDatabase("QSQLITE")
        connection.setDatabaseName(absPath("Contacts.db"))

        if not connection.open():
            print("No se puede conectar a la base de datos")
            sys.exit(1)

        model = QSqlTableModel()
        model.setTable("contacts")
        model.select()

        model.setHeaderData(0, Qt.Horizontal, "Id")
        model.setHeaderData(1, Qt.Horizontal, "Nombre")
        model.setHeaderData(2, Qt.Horizontal, "Empleo")
        model.setHeaderData(3, Qt.Horizontal, "Email")

        self.tabla.setModel(model)
        self.tabla.setColumnHidden(0, True)
        self.tabla.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
