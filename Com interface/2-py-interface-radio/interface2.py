import tkinter as tk

# sub biblioteca do tkinter com widgets mais modernos e estilizados
from tkinter import ttk

def atualizar_resultado():

    # obter o texto da caixa de entrada
    nome = caixa_texto.get()

    # obter a opção selecionada nos botões de rádio
    preferencia = var_radio.get()

    # verificar se a caixa de seleção de saudação informal está marcada
    if var_check_saudacao.get():
        saudacao = "Olá"
    else:
        saudacao = "Bem-vindo"

    if var_check_personalizada.get():
        saudacao += f"{saudacao}, caro(a)!"

    # obtera cor fav selecionada 
    cor_favorita = combo_cor.get()

    # montar mensagem final
    mensagem = f"{saudacao} {nome}! Você prefere {preferencia}."
    if cor_favorita:
        mensagem += f" Sua cor favorita é {cor_favorita}."

    # atualizar o rótulo com a mensagem final
    label_resultado.config(text=mensagem)

# ================================================================================
# criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Interface")
janela.geometry("400x150")
janela.config(bg='red') # cor de fundo da janela


# ================================================================================
# criar uma caixa de entrada (entry), equivalente ao input do html
# label é o textinho de cima e a caixa de texto é o entry
label_nome = tk.Label(janela, text="Digite seu nome: ")
label_nome.pack(pady=5)
caixa_texto = tk.Entry(janela, width=40)
caixa_texto.pack(pady=5)

# =================================================================================
# executar a janela
janela.mainloop()