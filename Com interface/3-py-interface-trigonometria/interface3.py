import tkinter as tk # importa a biblioteca tkinter para a criação da interface gráfica
import math # importa a biblioteca math para realizar operações matemáticas
from PIL import Image, ImageTk # importa as classes image e imagetk da biblioteca PIL para manipulação de imagens
import os # importa a biblioteca os para operações com o sistema de arquivos
import sys # importa a biblioteca sys para manipulação de variáveis e funções do sistema

def resource_path(relative_path):
    # obtém o caminho absoluto para o recurso, funciona tanto em ambiente de desenvolvimento quanto após o empacotamento com o pyinstaller
    try:
        # pyinstaller cria um diretório temporário e armazena o caminho em _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # se n estiver executando pelo pyinstaller, utiliza o caminho absoluto do diretório atual
        base_path = os.path.abspath(".")