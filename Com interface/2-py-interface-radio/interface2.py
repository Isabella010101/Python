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
        saudacao += ", caro(a)!"

    # obtera cor fav selecionada 
    cor_favorita = combo_cor.get()

    # montar mensagem final
    mensagem = f"{saudacao} {nome}! \nVocê prefere {preferencia}. "
    if cor_favorita:
        mensagem += f"Sua cor favorita é {cor_favorita}. "

    # atualizar o rótulo com a mensagem final
    label_resultado.config(text=mensagem)

# ===============================================================================
# função para limpar os campos de entrada
def limpar_campos():
    # lima todas as escolhas
    caixa_texto.delete(0, tk.END)
    var_radio.set("Café")
    var_check_saudacao.set(False)
    var_check_personalizada.set(False)
    combo_cor.set('Escolha uma cor')
    label_resultado.config(text="")

# ================================================================================
# criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Interface")
janela.geometry("400x550")
janela.config(bg='blue') # cor de fundo da janela


# ================================================================================
# criar uma caixa de entrada (entry), equivalente ao input do html
# label é o textinho de cima e a caixa de texto é o entry
label_nome = tk.Label(janela, text="Digite seu nome: ", bg='blue', fg='white', font=("Arial", 15, 'bold'))
label_nome.pack(pady=5)
caixa_texto = tk.Entry(janela, width=20, bg="black", fg="white", font=("Arial", 20, 'bold'))
caixa_texto.pack(pady=5)

# =================================================================================
# ----------------- Configuração dos Estilos -----------------
style = ttk.Style()
# Configura o estilo para os botões de rádio
style.configure('Custom.TRadiobutton', background='blue', foreground='white', 
                selectcolor='black', indicatorcolor='black', font=("Arial", 12, 'bold'))
# Configura o estilo para os botões de rádio quando o mouse está sobre eles
style.map('Custom.TRadiobutton',
          background=[('active', 'blue')],
          foreground=[('active', 'white')])

# =================================================================================
# criar botões de rádio para selecionar a preferência, apenas uma opção
label_preferencia = tk.Label(janela, text="Escolha a sua preferência: ", bg='blue', fg='white', font=("Arial", 15, 'bold'))
label_preferencia.pack(pady=5)

# radio - escolha para selecionar um só
var_radio = tk.StringVar(value="Café") 

radio_cafe = ttk.Radiobutton(janela, text="Café", variable=var_radio, value="Café", style='Custom.TRadiobutton')
radio_cha = ttk.Radiobutton(janela, text="Chá", variable=var_radio, value="Chá", style='Custom.TRadiobutton')
radio_suco = ttk.Radiobutton(janela, text="Suco", variable=var_radio, value="Suco", style='Custom.TRadiobutton')
radio_agua = ttk.Radiobutton(janela, text="Água", variable=var_radio, value="Água", style='Custom.TRadiobutton')

# para deixar visível
radio_cafe.pack()
radio_cha.pack()
radio_suco.pack()
radio_agua.pack()



# ================================================================================
# criar caixas de seleção (checkbox) - aceita mais de uma seleção
label_saudacao = tk.Label(janela, text="Escolha uma: ", bg='blue', fg='white', font=("Arial", 15, 'bold'))
label_saudacao.pack(pady=5)

var_check_saudacao = tk.BooleanVar()
check_saudacao = tk.Checkbutton(janela, text="Usar saudação informal", variable=var_check_saudacao, bg='blue', fg='black', font=("Arial", 12, 'bold'))
check_saudacao.pack(pady=5)

var_check_personalizada = tk.BooleanVar()
check_personalizada = tk.Checkbutton(janela, text="Usar saudação personalizada", variable=var_check_personalizada, bg='blue', fg='black', font=("Arial", 12, 'bold'))
check_personalizada.pack(pady=5)

# ================================================================================
# combobox (caixa de seleção com opções)
label_cor = tk.Label(janela, text="Selecione sua cor favorita: ", bg='blue', fg='white', font=("Arial", 15, 'bold'))
label_cor.pack(pady=5)

combo_cor = ttk.Combobox(janela, values=["Vermelho", "Azul", "Verde", "Amarelo", "Preto", "Branco"])
combo_cor.set('Escolha uma cor')
combo_cor.pack(pady=5)

combo_cor.config(font=("Arial", 12, 'bold'), width=15)

# =================================================================================
# criar botões (Frase e limpar)
botao_atualizar = tk.Button(janela, text="Atualizar", command=atualizar_resultado, bg='blue', fg='black', font=("Arial", 12, 'bold'))
botao_atualizar.pack(pady=10)

botao_limpar = tk.Button(janela, text="Limpar", command=limpar_campos, bg='orange', fg='black', font=("Arial", 12, 'bold'))
botao_limpar.pack(pady=10)

# =================================================================================
# exibição do resultado final (rótulo "label")
label_resultado = tk.Label(janela, text="", wraplength=350)
label_resultado.pack(pady=10)


# =================================================================================
# executar a janela
janela.mainloop()