import os
import win32print # pip install win32printing
import win32api # pip install win-api

lista_impressora = win32print.EnumPrinters(2)
impressora = lista_impressora[2]

win32print.SetDefaultPrinter(impressora[2])

caminho = r"C:\Users\Maicon\Documents\DeVops\imprimir"
lista_arquivos = os.listdir(caminho)

for arquivo in lista_arquivos:
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)

