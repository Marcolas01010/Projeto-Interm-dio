import tkinter
from tkinter import *
from tkinter import messagebox


tela1 = Tk()
tela1.title("Agenda [Força Aérea Portuguesa]")
tela1.geometry('500x600+500+50')
tela1.wm_resizable(width=False, height=False)



branco = "#F6F5F4"
verde_lima = "#40FA02"
azul= "#1F02FA"
preto= "#0C0C0C"
azul_escuro= "#0E0078"
branco= "#F5F5F6"
verde_escuro = "#1B6A33"
castanho = "#6A4B1B"


lb0= tkinter.Label(tela1, text="Agenda Militar [Força Aérea Portuguesa]", font="RudoBock",bg=verde_escuro,fg=branco)
lb0.place(width=490,height=50,x=10,y=-10)



lb1 = tkinter.Label(tela1, text= "Nome", font="Time10")
lb1.place(width=70,height=20,x=20,y=50)
input_nome= Entry(tela1, font='Time 10')
input_nome.place(width=250, height=20, x=100,y=50)

lb2= tkinter.Label(tela1, text= "Telémovel", font="Time10")
lb2.place(width=100,height=20,x=20,y=100)
input_nome2= Entry(tela1, font= 'Time10')
input_nome2.place(width=250,height=20, x=117,y=100)

lb3= tkinter.Label(tela1, text="Endereço",font="Time10")
lb3.place(width=95,height=20,x=20,y=150)
input_nome3= Entry(tela1, font= 'Time10')
input_nome3.place(width=250,height=20, x=117, y=150)

lb4= tkinter.Label(tela1,text= "Distrito", font="Time10")
lb4.place(width=95, height=20, x=20, y=215)
input_nome4= Entry(tela1, font= 'Time10')
input_nome4.place(width=150,height=20, x=117, y=215)

lb5=tkinter.Label(tela1,text="País",font="Time10")
lb5.place(width=95,height=20,x=260,y=215)
input_nome5= Entry(tela1, font= 'Time10')
input_nome5.place(width=100,height=20, x=345, y=215)

lb6=tkinter.Label(tela1,text="Email" , font= "Time10")
lb6.place(width=95,height=20,x=20,y=250)
input_nome6= Entry(tela1, font= 'Time10')
input_nome6.place(width=250,height=20, x=117, y=250)

def adicionar():
    nome = input_nome.get()
    telemovel = input_nome2.get()
    endereco = input_nome3.get()
    distrito = input_nome4.get()
    pais = input_nome5.get()
    email = input_nome6.get()
    with open("agenda.txt", "a", encoding="utf-8") as file1:
        file1.write(nome + "\n")
        file1.write(telemovel + "\n")
        file1.write(endereco + "\n")
        file1.write(distrito + "\n")
        file1.write(pais + "\n")
        file1.write(email + "\n")

        messagebox.showinfo("agenda","Cadastro Efetuado com Sucesso!")

        input_nome.delete('0','end')
        input_nome2.delete('0','end')
        input_nome3.delete('0','end')
        input_nome4.delete('0','end')
        input_nome5.delete('0','end')
        input_nome6.delete('0','end')

def pesquisar():
    nome = input_nome.get()

    with open("agenda.txt", "r") as arquivo :
        for linha in arquivo:
            if nome in linha:
                input_nome2 = (arquivo.readline())
                input_nome3 = (arquivo.readline())
                input_nome4 = (arquivo.readline())
                input_nome5 = (arquivo.readline())
                input_nome6 = (arquivo.readline())
                if portugal:
                    input_preço = (arquivo.readline())
                elif Alemanha:
                    input_preço = (arquivo.readline())
                    input_preço = (arquivo.readline())

                l_nome_busca = Label (tela1, text=nome, font= 'Time10', anchor='w')
                l_nome_busca.place(width=400 , height=30, x= 20 , y=360)
                l_telemovel_busca = Label(tela1 , text= input_nome2 , font= "Time10" , anchor= 'w')
                l_telemovel_busca.place(width=90, height=50 , x=20, y=390)
                l_endereco_busca= Label(tela1 , text=input_nome3 , font= "Time10", anchor= "w")
                l_endereco_busca.place(width=400 , height= 50 , x=20 , y=420)
                l_distrito_busca = Label(tela1, text= input_nome4, font= "Time10", anchor= "w")
                l_distrito_busca.place(width=400 , height= 50 , x=20 , y=450)
                l_pais_busca = Label (tela1 , text= input_nome5, font= "Time10" , anchor = "w")
                l_pais_busca.place(width=400 , height= 50 , x=20 , y=480)
                l_email_busca = Label(tela1, text= input_nome6 , font= "Time10", anchor= "w")
                l_email_busca.place(width=400, height=50, x=20 , y=510)


b_adicionar= Button(tela1, text= 'Adicionar', font='Time 10 bold', bg=azul_escuro,fg=branco, command=adicionar)
b_adicionar.place(width=70, height=40,x=70,y=300)
b_pesquisar= Button(tela1, text = 'Pesquisar', font= "Time 10 bold", bg=azul_escuro,fg=branco, command=pesquisar)
b_pesquisar.place(width=70, height=40, x=300, y=300)



tela1.mainloop()