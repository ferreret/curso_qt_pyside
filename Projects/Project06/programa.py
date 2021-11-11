from os import name
from PySide6 import QtWidgets
from ui_monitor import Ui_MainWindow
from functools import partial
import pyqtgraph as pg  # pip install pyqtgraph
import random


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sondas = [
            {'nombre': 'Sonda 1', 'valores': [], 'color': 'r', 'simbolo': 'o'},
            {'nombre': 'Sonda 2', 'valores': [], 'color': 'b', 'simbolo': '+'},
            {'nombre': 'Sonda 3', 'valores': [], 'color': 'g', 'simbolo': 'star'},
        ]

        for sonda in self.sondas:
            self.comboBox.addItem(sonda['nombre'])

        self.construirGrafico()
        self.pushButton.clicked.connect(self.nuevaLectura)
        self.pushButton_2.clicked.connect(partial(self.nuevaLectura, True))

    def construirGrafico(self):
        self.widget.addLegend()
        self.widget.setBackground('w')

        self.graficos = []

        for sonda in self.sondas:
            plot = self.widget.plot(sonda['valores'],
                                    name=sonda['nombre'],
                                    pen=pg.mkPen(sonda['color'], width=3),
                                    symbol=sonda['simbolo'],
                                    symbolBrush=sonda['color'],
                                    symbolSize=12)
            self.graficos.append(plot)

        # self.widget.plot(self.valores, name='Sonda 1', pen=pg.mkPen(
        #     'b', width=3), symbol='o', symbolBrush='b', symbolSize=12)
        # self.widget.plot(self.valores2, name='Sonda 2', pen=pg.mkPen(
        #     'r', width=3), symbol='+', symbolBrush='r', symbolSize=14)
        self.widget.showGrid(x=True, y=True)
        # self.widget.setXRange(0, 10)
        self.widget.setYRange(-20, 30)
        self.widget.setTitle('Monitor de Temperatura', size='24px')
        styles = {'color': '#000', 'font-size': '20px'}
        self.widget.setLabel('left', 'Temperatura', '°C', **styles)
        self.widget.setLabel('bottom', 'Horas', 'H', **styles)

    def nuevaLectura(self, autogenerar=False):
        if not autogenerar:
            indice = self.comboBox.currentIndex()
            temperatura = self.spinBox.value()
            self.sondas[indice]['valores'].append(temperatura)
            self.graficos[indice].setData(self.sondas[indice]['valores'])
        else:
            for index, sonda in enumerate(self.sondas):
                sonda['valores'].append(random.randint(-20, 30))
                self.graficos[index].setData(sonda['valores'])


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()
