import tkinter
from tkinter import *
from tkinter import messagebox


tela1 = Tk()
tela1.title("Calculadora de IMC")
tela1.geometry('500x500+250+50')
tela1.wm_resizable(width=False, height=False)

azul= "#2668B6"
azul_claro= "#07DC9C"
preto="#040B09"
branco = "#FAFDFC"
fundo= "#92FFD0"






lb1 = tkinter.Label(tela1, text="Calculadora de IMC", font="Arial 15", anchor="w", fg=azul)
lb1.place(width=300,height=50,x=160,y=15)

lb2 = tkinter.Label(tela1,text="Peso (Kg):",font="Time 15 ")
lb2.place(width=180,height=50,x=-20,y=70)
input_nome= Entry(tela1, font='Time 10')
input_nome.place(width=250, height=20, x=120,y=86)

lb3= tkinter.Label(tela1, text= "Altura (cm):",font="Time 15")
lb3.place(width=180,height=50,x=-20,y=120)
input_nome2 = Entry(tela1, font= 'Time 10')
input_nome2.place(width=250,height=20,x=140,y=135)




def calcular_imc():
    peso= float(input_nome.get())
    altura= float(input_nome2.get()) / 100
    imc= peso / (altura ** 2)
    texto = "IMC:" + str(round(imc,2))
    Label_resultado = Label(tela1,text=texto , font= "Arial 12")
    Label_resultado.place(x=60, y=200,width=300 , height=30)

    if imc<18.5:
        imagem_path = "Abaixo do peso normal.png"

    elif imc < 24.9:
        imagem_path = "Peso normal.png"

    elif imc < 29.9:
        imagem_path = "Execesso de Pese.png"

    elif imc < 39.9:
        imagem_path = "Obesidade Classe 1.png"

    else:
         imagem_path = "Obesidade Extrema.png"


    imagem= PhotoImage(file= imagem_path)
    label_imagem = Label(tela1, image= imagem)
    label_imagem.place(width=200,height=150,x=115,y=315)
    label_imagem.image = imagem




#yMaster Sir
#

CalcularIMC= Button(tela1,text="Calcular IMC", font="Time 13", fg=azul_claro, bg=branco,command=calcular_imc)
CalcularIMC.place(width=100,height=50,x=180,y=250)




tela1.mainloop()