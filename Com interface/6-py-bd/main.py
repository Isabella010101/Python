import customtkinter as ctk
import sqlite3
from tkinter import ttk
from PIL import Image, ImageTk
from user_operations import UserOperations
import os
import sys
from database import Database

# função para lidar com caminhos de recursos em diferentes ambientes (desenvolvimento e executável)
def resource_path(relative_path):
    try:
        # tenta obter o caminho base do executável criado pelo PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # se não estiver em um executável, usa o diretório atual
        base_path = os.path.abspath(".")
    # retorna o caminho absoluto combinando o caminho base e o relativo
    return os.path.join(base_path, relative_path)

def get_db_path():
    if getattr(sys, 'frozen', False):
        # se estiver rodando como executável
        application_path = os.path.dirname(sys.executable)

    else:
        # se estiver rodando em desenvolvimento
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(application_path, 'cadastro_simplificado.db')

# classe principal da interface gráfica
class TelaCadastro(ctk.CTk):
    def __init__(self):
        super().__init__()
        # usa o novo método para obter o caminho do banco de dados
        db_path = get_db_path()
        self.db = Database(db_path)
        self.user_operations = UserOperations(self.db, self)
        self.setup_ui()
        self.selected_user = None
        self.set_icon()

    # define o ícone da janela principal
    def set_icon(self):
        icon_path = resource_path("assets/inicio.ico")
        try:
            self.iconbitmap(icon_path)
        except:
            print(f'Não foi possível carregar o ícone: {icon_path}')

    # configura todos os elementos da interface do usuário
    def setup_ui(self):
        self.title("Cadastro e Lista de usuários")
        self.geometry("600x500")
        # carrega as imagens ára os modos claro e escuro
        self.light_image = ctk.CTkImage(Image.open(resource_path("assets/light_icon.png")), size = (20, 20))

        self.dark_image = ctk.CTkImage(Image.open(resource_path("assets/dark_icon.png")), size = (20, 20))

        # tenta carregar o ícone padrão
        try:
            icon_image = Image.open(resource_path("assets/inicio.png"))
            icon_photo = Image