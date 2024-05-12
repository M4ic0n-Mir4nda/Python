import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 300
        self.esquerda = 500
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        botao1 = QPushButton('Botão 1', self)
        botao1.move(200, 200)  # esquerda - topo
        botao1.resize(150, 80)  # largura - tamanho do botao
        botao1.setStyleSheet('QPushButton{background-color:#18f72e; font:bold; font-size: 20px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(450, 200)  # esquerda - topo
        botao2.resize(150, 80)  # largura - tamanho do botao
        botao2.setStyleSheet('QPushButton {background-color:#18f7b6; font:bold; font-size: 20px}')
        botao2.clicked.connect(self.botao2_click)
        self.label_1 = QLabel(self)
        self.label_1.setText("Ola Mundo!")
        self.label_1.move(100, 100)
        self.label_1.resize(250, 25)
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color: blue}')

        self.carro = QLabel(self)
        self.carro.move(50, 400)
        self.carro.resize(500, 200)
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label_1.setText('Carro 1 selecinado')
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color: blue}')
        self.carro.setPixmap(QtGui.QPixmap('carro1.png'))

    def botao2_click(self):
        self.label_1.setText('Carro 2 selecionado')
        self.label_1.setStyleSheet('QLabel {font:bold; font-size: 25px; color: red}')
        self.carro.setPixmap(QtGui.QPixmap('carro2.png'))


app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec())
