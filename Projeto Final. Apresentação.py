import tkinter
from tkinter import *
from tkinter import ttk

tela1 = Tk()
tela1.title("Dados de Modelos de Hypercarros.com.pt🚗")
tela1.geometry('550x580+350+0')
tela1.wm_resizable(width=False, height=False)


lb0_color = "#0F729A"
tela= "#BCBAB5"



lb0 = tkinter.Label(tela1,text="Dados de Modelos de Hypercarros🚗",font="Verdana",bg=lb0_color)
lb0.place(width=580,height=100,x=0,y=0)

fundo = tkinter.Label(tela1,bg=tela)
fundo.place(width=560,height=550,x=0,y=100)



lb1 = tkinter.Label(tela1, text= "Marca",font="Verdana",)
lb1.place(width=100,height=30,x=30,y=150)
lb1.marca = ttk.Combobox(tela1 , text='Marca:',font= 'Time 12 bold',justify=CENTER)
lb1.marca.place (width=115, height=35,x=135,y=150)

lb2 = tkinter.Label(tela1, text='Modelo',font="Verdana")
lb2.place(width=100,height=30,x=275,y=150)
lb2.modelo = ttk.Combobox(tela1,text='Modelo:',font='Verdana')
lb2.modelo.place(width=115,height=35,x=385,y=150)

lb3_pais = tkinter.Label(tela1,text='País',font='Verdana')
lb3_pais.place(width=100,height=30,x=30,y=300)
lb3_pais = ttk.Combobox(tela1,text='País',font='Verdana')
lb3_pais.place(width=115,height=35,x=135,y=300)








tela1.mainloop()