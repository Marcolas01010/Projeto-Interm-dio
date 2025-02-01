import random

def escolher_palavra():
    palavras = ["casa","carro","floresta","montanha","navio"]
    return random.choice(palavras)
def jogar():
    palavra = escolher_palavra()

    #print(palavra)
    letras_adivinhadas = []
    tentativas = 6
    palavra_oculta = ["_"for _ in palavra]
    print("\nBem-vindo ao jogo da forca!")
    print ("O seu numero de vida é 6. Se acabar, é Game Over.")


    #Criar lista de letras adivinhadas
    while tentativas > 0:
        print ("\nPalavra:","".join(palavra_oculta))
        letra = input ("Escolha uma letra:").lower ()

        if letra in letras_adivinhadas:
            print("Errado! A letra não está na palavra")
            tentativas -=1
            continue


        letras_adivinhadas.append(letra)

        if letra in palavra:
            print('Boa! Essa letra corresponde na palavra !')
        else:
            print("Não! essa letra não está na palavra")

            palavra_adivinhada= True
            for i in palavra:
                if i not in letras_adivinhadas:
                    palavra_adivinhada = False
                    break


jogar()




