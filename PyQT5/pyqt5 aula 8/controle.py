from PyQt5 import uic,QtWidgets

def funcao_principal():
    if form.radioButton.isChecked():
        opcao = "Azul selecionada"
    elif form.radioButton_2.isChecked():
        opcao = "Vermelha selecionada"
    elif form.radioButton_3.isChecked():
        opcao = "Amarela selecionada"
    elif form.radioButton_4.isChecked():
        opcao = "Cinza selecionada"
    else:
        opcao = ""
    
    form.label_3.setText(opcao)

app = QtWidgets.QApplication([])
form = uic.loadUi("janela.ui")
form.pushButton.clicked.connect(funcao_principal)

form.show()
app.exec()