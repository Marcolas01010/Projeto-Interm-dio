import tkinter
from tkinter import *
from tkinter import messagebox


tela1 = Tk()
tela1.title("Agenda")
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




def adicionar():
    nome= input_nome.get()











b_adicionar= Button(tela1, text= 'Adicionar', font='Time 10 bold', bg=azul_escuro,fg=branco)
b_adicionar.place(width=70, height=40,x=70,y=300)
b_pesquisar= Button(tela1, text = 'Pesquisar', font= "Time 10 bold", bg=azul_escuro,fg=branco)
b_pesquisar.place(width=70, height=40, x=300, y=300)

lb0= tkinter.Label(tela1, text="Agenda", font="RudoBock",bg=verde_escuro,fg=branco)
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




tela1.mainloop()



