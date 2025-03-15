with open("ficheiro.txt", "w",encoding="utf-8") as file1:
    #ler o conteúdo todo
    file1.write("Marcos\nMatheus \nBernardo \nMiguel \nLuciano")

def escrever():
    with open("ficheiro.txt", "r", encoding="utf-8") as file1:
        conteudo = file1.readlines()
        for linha in conteudo:
            print(linha)



def contar():
    with open("ficheiro.txt", "r", encoding="utf-8") as file1:
        soma = 0
        conteudo = file1.readlines()
        for i in conteudo:
            soma+=1
        print(soma)


def criar_ficheiro():
    nome_ficheiro = input("Qual será o nome do ficheiro:")
    nome_completo= f"{nome_ficheiro}.txt"
    with open (nome_completo, "w") as ficheiro:
        pass
    print(f"Ficheiro {nome_completo} criado com sucesso!")



def inserir_frase():
    pedir_ficheiro = input("Qual é o ficheiro que quer abrir :")
    ficheiro_pedido= f"{pedir_ficheiro}.txt"
    frase = input(" Oque quer escrever no ficheiro ?")

    with open (pedir_ficheiro, "a") as ficheiro_frase :
        print(" a mensagem :",frase, "Foi escrita com sucesso")
        ficheiro_frase.write(frase + "\n")



def ler_ficheiro():
    ficheiro_leitura= input("Qual ficheiro que gostaria de ler ")
    leitura_ficheiro = f"{ficheiro_leitura}.txt"

    with open (ficheiro_leitura , "r") as leitura_ficheiro:
       leitura = leitura_ficheiro.read()
    if ficheiro_leitura:
        print("\nConteúdo do Ficheiro :")
        print(leitura)
    else:
        print(f"O ficheiro {leitura_ficheiro} está vazio")


def menu():
    while True:
        print("\n Menu:")
        print("1- Criar um ficheiro")
        print("2- Inserir um frase num ficheiro")
        print("3- Ler conteúdo de um ficheiro")
        print("-4 Sair")

        opcao = input("Qual é a opção que quer escolher ?")


        if opcao == "1" :
            criar_ficheiro()

        elif opcao == "2" :
            inserir_frase()

        elif opcao== "3":
            ler_ficheiro()

        elif opcao == "4":
            print("Saiu...")
            break

menu()