produtos = ["Banana", "Maçã", "Arroz"]
precos = [1.0, 1.5, 5.0]
quantidade = [50, 30, 20]
carrinho_produtos = []
carrinho_quantidade = []


#produtos disponiveis
#produtos_disponiveis = [
    #{"id": 1, "nome": "banana", "preco": 1.0},
    #{"id": 2, "nome": "Maçã", "preco": 1.5},
    #{"id": 3, "nome": "arroz", "preco": 5.0}
#]

#def remover_produto(lista, nome_produto):
    #return [produto for produto in lista if produto["nome"] != nome_produto]


def exibir_stock():
    exibir_stock = print("Produtos",produtos,"preços",precos,"quantidade",quantidade)


def adicionar_ao_carrinho():
    produto = input("Qual produto queres adicionar")
    if produto not in  produtos :
        print("Esse produto não esta na loja")
    else:
        indice = produtos.index(produto)
        if produto not in carrinho_produtos:
            carrinho_produtos.append(produto)
        unidades = int(input("Qual a quantidade do produto ?"))
        if unidades>quantidade[indice]:
            print("Essa quantidade não esta na loja")
            carrinho_quantidade.append(quantidade)
            unidades[indice]-=quantidade
        if carrinho_quantidade [indice]:
            carrinho_quantidade[indice] += quantidade
            unidades[indice] -= quantidade
            print("O produto foi adicionado ao carrinho com sucesso!")


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
        exibir_stock()
    elif opcao == "2":
        adicionar_ao_carrinho()
    elif opcao == "3":
        remover_do_carrinho()
    elif opcao == "4":
        finalizar_compra()
    elif opcao == "5":
        adicionar_stock()

    elif opcao == "6":
        print("Saiu...")
        break


