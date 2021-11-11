import sys
from helpers import absPath
from PySide6.QtSql import QSqlDatabase, QSqlQuery

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName(absPath("Contacts.db"))

if not connection.open():
    print("No se puede conectar a la base de datos")
    sys.exit(1)

query = QSqlQuery(connection)
query.exec("DROP TABLE IF EXISTS contacts")
query.exec("""CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            nombre VARCHAR(40) NOT NULL,
            empleo VARCHAR(50),
            email VARCHAR(40) NOT NULL)
            """)

nombre, empleo, email = "Héctor", "Instructor", "hektor@ejemplo.com"

query.exec(f"""
    INSERT INTO contacts (nombre, empleo, email)
    VALUES ('{nombre}', '{empleo}', '{email}')
""")

contacts = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

query.prepare("INSERT INTO contacts (nombre, empleo, email) VALUES (?,?,?)")

for nombre, empleo, email in contacts:
    print(nombre)
    query.addBindValue(nombre)
    query.addBindValue(empleo)
    query.addBindValue(email)
    query.exec()

query.exec("SELECT nombre, empleo, email FROM contacts")

# if query.first():
#     print(query.value("nombre"), query.value("empleo"), query.value("email"))

while query.next():
    print(query.value("nombre"), query.value("empleo"), query.value("email"))

connection.close()

print("Conexión cerrada?", not connection.isOpen())
