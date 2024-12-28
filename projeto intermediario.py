produtos = ["Banana", "Maçã", "Arroz"]
precos = [1.0, 1.5, 5.0]
stock = [50, 30, 20]

#def remover_produto(lista, nome_produto):
    #return [produto for produto in lista if produto["nome"] != nome_produto]


def exibir_stock():
    exibir_stock = print(produtos)


def adicionar_ao_carrinho():
    input("Qual produto queres adicionar")

def remover_do_carrinho():
    input("Qual produto gostaria de remover do carrinho")

def finalizar_compra():
    print("Voce finalizou a compra")

def adicionar_stock():
    input("Qual produto gostaria de adicionar no stock")

# Menu principal
while True:
    print("\n1. Ver Stock\n2. Comprar Produto\n3. Remover do Carrinho\n4. Finalizar Compra\n5. Adicionar Stock\n6. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        exibir_stock= print(produtos,precos,stock)
    elif opcao == "2":
        adicionar_ao_carrinho = input ("Qual produto queres adicionar297673")
    elif opcao == "3":
        remover_do_carrinho = input ("Qual produto gostaria de remover do carrinho")
    elif opcao == "4":
        finalizar_compra = print ("Voce finalizou a compra")
    elif opcao == "5":
        adicionar_stock = input ("Qual produto gostaria de adicionar no stock")

    elif opcao == "6":
        break

