import os

restaurantes = []

#Dicionarios uma coleção de informação para um unico item
#restaurantes = [{"Nome":"", "Categoria":"","Ativo":False},{""}]
def exibir_nome_programa():
    """
    Exibe o nome do programa com a formatação do print a seguir
    """
    print("""
    ███████████████████████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄███▄─▄▄▀█─▄▄─███▄─▀█▀─▄█▄─██─▄█▄─▀█▄─▄█▄─▄▄▀█─▄▄─█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄██─▄█▀█▄▄▄▄─████─██─█─██─████─█▄█─███─██─███─█▄▀─███─██─█─██─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀
    """) 
    #print(""""
    #as 3 "" foram o trabalho de manter o estilo do texto e pular a linhas q tiverem dentro 
    #delas
    #""")
def exibir_opcoes():
    """Opções a serem mostradas na aplicação"""
    print("1. Cadastrar Restaurantes")
    print("2. Listar Restaurantes")
    print("3. Alterar estado do Restaurante")
    print("4. Sair\n")

def voltar_menu_principal():
    """
    retorno para o menu
    
    Outputs:
    Retorna ao menu principal
    """
    print("Retornando ao menu....\n")
    input("Digite uma tecla para voltar ao menu principal  ")
    main()

def exibir_subtitulo(texto):
    #windows
    os.system("cls")
    #Mac
    #os.system("clear")
    linha ="*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)

#def == function no java
def opcao_invalida(): 
    """
    Exibe mensagem de erro e retorna ao menu
    
    Outputs:
    Retorna ao menu principal
    """
    print("Opção Inválida\n")
    voltar_menu_principal()
def finalizar_app():
        """Exibe mensagem de finalizar app"""
        exibir_subtitulo("Finalizando o App...")


def continuar_resgistro():
    """
    Responsavel em manter o cadastro para outra entrada
        
        Inputs:
        opção do registro = 1, 2 ou qualquer outro caractere

        Outputs:
        opção do registro == 1  recomeça o cadastro para outro restaurante
        opção do registro == 2  Abre a lista dos restaurantes cadastrados
        qualquer outra opção, retorna ao menu principal
        """
    try:
        opcao_registro =int(input("Continuar o registrando ou ver lista? Digite 1 para registrar, 2 para visualizar lista e qualquer outra tecla para retornar ao menu   "))
        if opcao_registro == 1 :
            cadastrar_novo_restaurante()
        elif opcao_registro == 2:
            listar_restaurantes()
        else:
            voltar_menu_principal()
    except:
        voltar_menu_principal()

def cadastrar_novo_restaurante():
    """"
    Essa função é responsável por cadastrar um novo 
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    """
    exibir_subtitulo("Cadastre o Restaurante\n")
    nome_do_restaurante = input("Digite o nome a ser registrado: ")
    categoria = input(f"Categoria do Restaurante {nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante,"categoria":categoria,"ativo":False}
    restaurantes.append(dados_do_restaurante)
    #restaurantes.append(nome_do_restaurante)
    print(f"O restaurante: {nome_do_restaurante} foi cadastrado!\n")
    continuar_resgistro()
   
def listar_restaurantes():
    """
    Lista os restaurantes presentes na lista
    
    Outputs:
    Lista de restaurantes na tela
    """
    exibir_subtitulo("Lista de Restaurantes\n")
    #len serve para saber a qtd de itens existe na lista
    if len(restaurantes)>=1:
        print(f"{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
        for restaurante in restaurantes:
            nome_restaurante = restaurante["nome"]
            categoria = restaurante["categoria"]
            ativos = "ativado" if restaurante["ativo"] else "desativado"
            #ljust(x) limita a qtd de caracteres serão mostrados, x sendo o valor escolhido
            print(f"{restaurantes.index(restaurante)+1}.{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativos}")
            #print(f"{restaurantes.index(restaurante)+1}.{restaurante}")
    else:
        print("Não há nenhum restaurante listado ;-;")
        try:
            opcao_lista =int(input("Deseja cadastrar um restaurante? 1 para sim e qualquer tecla não   "))
            if opcao_lista == 1:
                cadastrar_novo_restaurante()
            else:
                voltar_menu_principal()
        except:
            voltar_menu_principal()
    voltar_menu_principal()
        
def alternar_estado_restaurante():
   """
   Altera o estado de ativo/desativado de um restaurante da lista

   Inputs:
   nome do restaurante

   Outputs:
   Exibe mensagem de sucesso da alteração ou de restaurante não ter sido encontrado e 
   retorna ao menu principal
   """
   exibir_subtitulo("Alterar estado do restautante")
   nome_restaurante = input("Digite o nome do Restaurante que deseja Alterar: ")
   restaurante_encontrado = False

   for restaurante in restaurantes :
       if nome_restaurante == restaurante ["nome"]:
           restaurante_encontrado = True
           restaurante["ativo"] = not restaurante["ativo"]
           #Térnario a variavel recebe o que é pra ser feito if restaurante["ativo"] else
           # o mesmo para o falso 
           mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante}foi desativado com sucesso"
           print(mensagem)
   escolher_estado = int(input("Deseja ver a lista ou Encerrar o APP?\nDigite 1 para ir a lista e qualquer tecla para encerrar  "))
   try:
        if escolher_estado == 1:
            listar_restaurantes()
        else:
           finalizar_app()
   except:
        finalizar_app()        
   if not restaurante_encontrado:
       print(f"Restaurante {nome_restaurante} não encontrado")
       voltar_menu_principal()

    
    
def escolher_opcoes():
    """
    Solicita e excuta a opção a ser escolhida

    Inputs:
    opção

    Output:
    Executa a opção escolhida
    """
    
    try:
        opcao_escolhida = int(input("Escolha uma das opções: "))
        #   opcao_escolhida = int(opcao_escolhida)
        #print(f"") junta as variaveis na linha com os conchetes 
        print(f"Você escolheu a opção {opcao_escolhida}")
        #IF não precisa de parenteses para a condição e logo apos dela vem o : caso verdadeiro
        #ELIF == ELSE IF 
        if opcao_escolhida == 1 :
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :
            listar_restaurantes()
        elif opcao_escolhida == 3 :
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            #print("Finalizar o programa...")
            finalizar_app()
            pass
        else:
            opcao_invalida()
    except:
        opcao_invalida()



#def escolher_opcoes():
#match substitui os elif por case(casos)
#    def escolher_opcoes_match():
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                print('Adicionar restaurante')
            case 2:
                print('Listar restaurantes')
            case 3:
                print('Ativar restaurante')
            case 4:
                print('Finalizar app')
            case _:
                print('Opção inválida!')



def main():
    """
    Função principal que inicia o programa
    """
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ =="__main__":
    main()