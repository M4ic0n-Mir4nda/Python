import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 300
        self.esquerda = 500
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


app = QApplication(sys.argv)
j = Janela()
sys.exit(app.exec())
