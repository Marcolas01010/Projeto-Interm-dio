
print('-=' *12)
print("manipulação de Dados")



def cadastrar():
    nome = input ("Qual seu nome ?")
    idade= input ("Qual sua idade")
    with open("lista_idades.txt", "a",encoding="utf-8") as file1:
        file1.write(nome + "\n")
        file1.write (str(idade) +"\n")

        print(f"{nome} foi cadastrado com {idade} anos.\n")

def buscar():
       nome = input ("Procurar idade de :")
       with open ("Lista_idades.txt",'r') as file1:
           for linha in file1:
               if nome in linha:
                   print("idade:"+ file1.readline())





while True:
    print("0-sair\n1-Cadastrar\n2- Buscar")
    opcao = input("Opção desejada:")

    if opcao == "0":
        print("Saíste do Programa")
        break

    if opcao == "1":
        cadastrar()

    if opcao =="2":
        buscar()



