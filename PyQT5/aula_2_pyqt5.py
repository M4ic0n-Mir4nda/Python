import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 300
        self.esquerda = 500
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        botao1 = QPushButton('Botão 1', self)
        botao1.move(150, 200)  # esquerda - topo
        botao1.resize(150, 80)  # largura - tamanho do botao
        botao1.setStyleSheet('QPushButton{background-color:#18f72e; font:bold; font-size: 20px}')
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(150, 400)  # esquerda - topo
        botao2.resize(150, 80)  # largura - tamanho do botao
        botao2.setStyleSheet('QPushButton{background-color:#18f7b6; font:bold; font-size: 20px}')
        botao2.clicked.connect(self.botao2_click)
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        print('Botão 1 foi clicado!')

    def botao2_click(self):
        print('Botão 2 foi clicado!')


app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec())
