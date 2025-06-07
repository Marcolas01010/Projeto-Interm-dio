import tkinter
from tkinter import *
from tkinter import ttk

tela1 = Tk()
tela1.title("Dados de Modelos de Hypercarros.com.pt🚗")
tela1.geometry('550x580+350+0')
tela1.wm_resizable(width=False, height=False)


lb0_color = "#0F729A"
tela= "#BCBAB5"



def atualizar_eventos(event):
    marca_selecionada = comb_marca.get()  # ← Pega o texto da marca selecionada
    modelos = marcas_modelos.get(marca_selecionada, [])
    comb_modelo['values'] = modelos
    comb_modelo.set('')



lb0 = tkinter.Label(tela1,text="Dados de Modelos de Hypercarros🚗",font="Verdana",bg=lb0_color)
lb0.place(width=580,height=100,x=0,y=0)

fundo = tkinter.Label(tela1,bg=tela)
fundo.place(width=560,height=550,x=0,y=100)


marcas_modelos = {
    "Lamborghini": ["Aventador", "Huracan", "Gallardo", "Revuelto","Urus"],
    "Mercedes": ["AMG GT", "S63", "G63", "Project One"],
    "Bmw": ["M3", "M4", "i8", "Z4"],
    "Mclaren": ["P1", "720S", "600LT", "F1"],
    "Ferrari": ["LaFerrari", "488 Pista", "F40", "Enzo Ferrari"]

}





lb1 = tkinter.Label(tela1, text= "Marca",font="Verdana",)
lb1.place(width=100,height=30,x=30,y=150)
comb_marca = ttk.Combobox(tela1 , text='Marca:',font= 'Time 12 bold',justify=CENTER)
comb_marca.bind("<<ComboboxSelected>>", atualizar_eventos)
comb_marca.place (width=122, height=35,x=135,y=150)
comb_marca['values'] = ("Lamborghini", "Ferrari","Mclaren","Bmw","Mercedes")

lb2 = tkinter.Label(tela1, text='Modelo',font="Verdana")
lb2.place(width=100,height=30,x=275,y=150)
comb_modelo = ttk.Combobox(tela1,text='Modelo:',font='Verdana')
comb_modelo.place(width=148,height=35,x=385,y=150)

lb3_pais = tkinter.Label(tela1,text='País',font='Verdana')
lb3_pais.place(width=100,height=30,x=25,y=275)
comb_pais = ttk.Combobox(tela1,text='País',font='Verdana')
comb_pais['values'] = "Portugal","Alemanha","França","Inglaterra","Brasil","Estado Unidos","Emirado Árabes"
comb_pais.place(width=175,height=35,x=135,y=275)








tela1.mainloop()