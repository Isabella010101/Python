# importação de biblioteca necessárias
# biblioteca os - operation system que permite rodar comando para mexer no sistema, editar, criar, excluir, poder fazer o crud
import os

# lista de dicionários representando os restaurantes
# no python, chamamos array de dicionário
restaurantes = [
    {'nome':'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True}, 
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

# -------------------------------------------------------------------------------------Funções de exibição e utilitárias

# camelCase - nomes com mistura de maiúsculas e minúsculas
# snake_case - utilizamos underline para separar cada palavra, utilizamos essa forma no python por padrão
def exibir_nome_do_programa():
    # três aspas serve para colocar um comentário ou print em várias linhas
    print("""        
        █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
        ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls') #limpa a tela (funciona apenas no windows)

    # estilizar com ******** dependendo da quantidade de letras no texto
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opcao():

    """
    Função para processar a escola do usuário no menu principal
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        # == - q nem no php, para ver se é igual string ou int msm, === - mais restrito para o tipo de dado até, = - passar valor
        if opcao_escolhida == 1:
            # print('Opção 1 escolhida!\n')
            # voltar_ao_menu_principal()
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            # print('Opção 2 escolhida!\n')
            listar_restaurantes()

        elif opcao_escolhida == 3:
            # print('Opção 3 escolhida!\n')
            # voltar_ao_menu_principal()
            alternar_estado_do_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except:
        opcao_invalida()



# ---------------------------------------------------------------------------------------Funções principais do programa

# 
def cadastrar_novo_restaurante():
    """
    Função para processar um novo restaurante

    inputs:
    - nome do restaurante
    - categoria

    outputs:
    - adiciona um novo restaurante à lista de restaurantes
    """
    exibir_subtitulo('Cadastro de novos restaurantes\n')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')

    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Função para listar todos os restaurantes cadastrados
    """

    exibir_subtitulo('Listando os restaurantes\n')

    print(f'{'nome_restaurante'.center(21)} | {'categoria'.center(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        # ljust - left justify 20 characteres no máximo por linha
        print(f'-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """
    Função para ativar ou desativar um restaurante
    """

    exibir_subtitulo('Alternando estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # inverte o estado (ex. false para true)
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
    
    voltar_ao_menu_principal()


# função main sempre tem que estar como último item do script
def main():
    """
    Função para processar a escolha do usuário no menu principal
    """
    os.system('cls') # limpa a tela
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

# padrão para qualuer sistema de python, define o main como main
if __name__ == '__main__':
    main()
