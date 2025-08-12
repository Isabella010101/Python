import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
import sys
from PIL import Image, ImageTk

def resource_path(relative_path):
    # obtém o caminho absoluto para o recurso, funciona para dev e para o Pyinstaller

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class FormularioInscricao:
    def __init__(self, master):
        self.master = master
        self.master.title("Formulário de Inscrição")
        self.master.geometry("500x400")

        # configurando o ícone da janela
        self.set_icon()

        # lista de temas disponíveis no ttkbootstrap
        # (https://ttkbootstrap.readthedocs.io/en/latest/themes)
        self.temas = ["darkly", "flatly", "litera", "minty", "superhero", "yeti", "cosmo", "cyborg", "journal", "lumen", "sandstone", "united", "pulse", "morph", "solar", "vapor"]

        # configuração do estilo inicial
        self.style = ttk.Style("darkly")

        # criação do frame principal
        self.frame = ttk.Frame(self.master, padding=20)
        self.frame.pack(fill=BOTH, expand=YES)

# ==========================================================================================================================================================================================
        # título
        ttk.Label(self.frame, text="Formulário de Inscrição", font=("TkDefaultFont", 16, "bold")).pack(pady=10)

# ==========================================================================================================================================================================================
        # campo nome
        ttk.Label(self.frame, text="Nome").pack(anchor=W, pady=(10, 0))
        self.nome_entry = ttk.Entry(self.frame, width=50)
        self.nome_entry.pack(fill=X)

# ==========================================================================================================================================================================================
        # campo email
        ttk.Label(self.frame, text="Email").pack(anchor=W, pady=(10, 0))
        self.email_entry = ttk.Entry(self.frame, width=50)
        self.email_entry.pack(fill=X)

# ==========================================================================================================================================================================================
        # campo idade
        ttk.Label(self.frame, text="Idade").pack(anchor=W, pady=(10, 0))
        self.idade_entry = ttk.Entry(self.frame, width=50)
        self.idade_entry.pack(fill=X)

# ==========================================================================================================================================================================================
        # frame para checkbox e combox
        self.opcoes_frame = ttk.Frame(self.frame)
        self.opcoes_frame.pack(fill=X, pady=10)

        # checkbox lembrar dados
        self.lembrar_var = ttk.BooleanVar()
        self.lembrar_check = ttk.Checkbutton(self.opcoes_frame, text="Lembrar dados?", variable=self.lembrar_var, bootstyle="round-toggle")
        self.lembrar_check.pack(side=LEFT)

        # comboboxpara seleção de temas
        self.tema_var = ttk.StringVar()
        self.tema_combo = ttk.Combobox(self.opcoes_frame, textvariable=self.tema_var, values=self.temas, state="readonly", width=15)
        self.tema_combo.set("darkly") #tema inicial
        self.tema_combo.pack(side=RIGHT)
        self.tema_combo.bind("<<ComboboxSelected>>", self.mudar_tema)

# ==========================================================================================================================================================================================
        # frame para os botões
        self.botoes_frame = ttk.Frame(self.frame)
        self.botoes_frame.pack(pady=20, fill=X)

        # botão enviar
        self.enviar_btn = ttk.Button(self.botoes_frame, text="Enviar", bootstyle ="succes", command=self.enviar)
        self.enviar_btn.pack(side=LEFT, padx=5)

        # botao cancelar
        self.cancelar_btn = ttk.Button(self.botoes_frame, text="Cancelar", bootstyle="danger", command=self.cancelar)
        self.cancelar_btn.pack(side=LEFT, expand=True)

# ==========================================================================================================================================================================================
        # frame para exibir os dados coletados
        self.dados_frame = ttk.Frame(self.frame)
        self.dados_frame.pack(pady=10, fill=X)

        # labels para exibir os dados coletados
        self.nome_label = ttk.Label(self.dados_frame, text="", anchor=CENTER)
        self.nome_label.pack(fill=X)

        self.email_label = ttk.Label(self.dados_frame, text="", anchor=CENTER)
        self.email_label.pack(fill=X)

        self.idade_label = ttk.Label(self.dados_frame, text="", anchor=CENTER)
        self.idade_label.pack(fill=X)

        self.lembrar_label = ttk.Label(self.dados_frame, text="", anchor=CENTER)
        self.lembrar_label.pack(fill=X)
    
# =========================================================================================================================================================================================
    # ícone
    def set_icon(self):
        icon_ico = resource_path("logo.ico")
        icon_png = resource_path("logo.png")

        if os.path.exists(icon_ico):
            self.master.iconvitmap(icon_ico)
        elif os.path.exists(icon_png):
            logo = Image.open(icon_png)
            logo = ImageTk.PhotoImage(logo)
            self.master.iconphoto(True, logo)
        else:
            print("AArquivo de ícone não encontrado.")

    def enviar(self):
        # atualiza as labels com os dados coletados
        self.nome_label.config(text=f'Nome: {self.nome_entry.get()}')
        self.email_label.config(text=f'Email: {self.email_entry.get()}')
        self.idade_label.config(text=f'Idade: {self.idade_entry.get()}')
        # atualiza o status do checkbox lembrar dados
        self.lembrar_label.config(text=f'Lembrar dados: {'Sim' if self.lembrar_var.get() else 'Não'}')

    def cancelar(self):
        # limpa os campos de entrada e as labels
        self.nome_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.idade_entry.delete(0, END)
        self.lembrar_var.set(False)

        self.nome_label.config(text="")
        self.email_label.config(text="")
        self.idade_label.config(text="")
        self.lembrar_label.config(text="")

    def mudar_tema(self, event):
        # função para mudar o tema quando um novo é selecionado no combobox
        novo_tema = self.tema_var.get()
        self.style.theme_use(novo_tema)

if __name__ == "__main__":
    root = ttk.Window()
    app = FormularioInscricao(root)
    root.mainloop()

