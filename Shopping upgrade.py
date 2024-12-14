
lista= "Bananas [50 Unidades|preço 1.99] || Arroz [30 Unidades|preço 2.99] ||  Feijão [20 Unidades]|3.99"
lista_unidade = [50 ,30, 20]
lista_preco =  [.99,  2.99,3.99]
lista_carrinho = []
def ver_stock():
    print("")
def comprar_produto():
    print("")
def remover_carrinho():
    print("")
def finalizar_compra():
    print("")
def adicionar_stock():
    print("")





while True:
    print ("1. Ver Stock\n 2. Comprar produto \n 3. Remover do carrinho \n 4. Finalizar compra \n 5. Adicionar Estoque \n 6. Sair")
    escolha = input ("Escolha uma opção")
    if escolha == "1":
        ver_stock()
    elif escolha == "2":
        comprar_produto(lista_preco+lista)
    elif escolha == "3":
        remover_carrinho()
    elif escolha == "4":
        finalizar_compra()
    elif escolha == "5":
         adicionar_stock()
    elif escolha == "6":
        print ("Sair")
        break

