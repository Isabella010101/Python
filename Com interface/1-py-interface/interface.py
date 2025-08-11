import tkinter as tk

def mostrar_mensagem():
    # obter o texto da caixa de texto
    texto = caixa_texto.get()

    # atualizar o rótulo com o texto obtido
    label_resultado.config(text=texto)

# ================================================================================
# criar a janela principal
janela = tk.Tk()
janela.title("Exemplo de Interface")
janela.geometry("400x150")
janela.config(bg='red') # cor de fundo da janela


# ================================================================================
# criar uma caixa de entrada (entry), equivalente ao input do html
caixa_texto = tk.Entry(janela, width=20, bg="black", fg="white", font=("Arial", 20))
caixa_texto.pack(pady=5)


# =================================================================================
# criar um botão, bg-background, fg-cor da fonte
botao = tk.Button(janela, text="Mostrar Texto", command=mostrar_mensagem, bg="blue", fg="white")
botao.pack(pady=5)


# ==================================================================================
# criar um rótulo (label) para mostrar o resultado
label_resultado = tk.Label(janela, text="", bg="red", font=("Arial", 20), fg="white")
# pady - y-vertical padding
label_resultado.pack(pady=10)


# =================================================================================
# executar a tela principal, um loop infinito para manter a janela aberta
janela.mainloop()