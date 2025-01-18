produtos = ["Banana", "Maçã", "Arroz"]
precos = [1.0, 1.5, 5.0]
quantidade = [50, 30, 20]
carrinho_produtos = []
carrinho_quantidade = []
def exibir_stock():
    print("\nProdutos:", produtos)
    print("Preços:", precos)
    print("Quantidade em estoque:", quantidade)
def adicionar_ao_carrinho():
    produto = input("Qual produto queres adicionar")
    if produto not in produtos:
        print("Esse produto não esta na loja")
    else:
        indice = produtos.index(produto)
        unidades = int(input("Qual a quantidade do produto ?"))
        if unidades > quantidade[indice]:
            print("Essa quantidade não esta na loja")
        if produto not in carrinho_produtos:
            carrinho_produtos.append(produto)
            carrinho_quantidade.append(unidades)
            print("O produto foi adicionado ao carrinho com sucesso!")
        else:
            indice_carrinho = carrinho_produtos.index(produto)
            carrinho_quantidade[indice_carrinho] += unidades
            print("O produto foi adicionado ao carrinho com sucesso!")
        quantidade[indice] -= unidades
def remover_do_carrinho():
    produto_remover= input("Qual produto gostaria de remover do carrinho")
    if produto_remover not in carrinho_produtos:
        print("Esse produto não esta na loja")
    else:
        indice = carrinho_produtos.index(produto_remover)
        quantidade_removida = carrinho_quantidade[indice]
        carrinho_produtos.remove(produto_remover)
        carrinho_quantidade.remove(quantidade_removida)
        indice_loja = produtos.index(produto_remover)
        quantidade[indice_loja]+=quantidade_removida

        print(f"O produto '{produto_remover}'foi removido do carrinho. Quantidade removida :{quantidade_removida}")

def finalizar_compra():
    print("Voce finalizou a compra")

def adicionar_stock():
   produto = input("Qual produto gostaria de adicionar no stock")
   if produto not in produtos :
       produtos.append(produto)
       preco =float(input("Qual é o preço do produto"))
       precos.append(preco)
       quantidade_nova= int(input("Qual é a quantidade Inicial ?"))
       quantidade.append(quantidade_nova)
       print(f"O produto '{produto}' foi adicionado ao estoque com {quantidade_nova} unidades.")

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
