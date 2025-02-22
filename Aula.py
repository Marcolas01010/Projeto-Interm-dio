import tkinter as tk
root = tk.Tk()

azul='#0001ff'
verde='#00ff2e'
preto= '#000000'
vermelho= '#ff0000'


root.title("Sharkcoders")
root.geometry("500x300+200+200")
root.configure(background=verde)

def fundo1():
    root.configure(background=azul)
    lt1.configure(text= 'Azul',background=azul)

lt1 = tk.Label(root, text= 'Azul', font= 'Arial 14 bold')

def fundo2():
    root.configure(background=verde)
    lt1.configure(text='Verde', background=verde)

    lt2= tk.Label(root, text= 'Verde', font= 'Arial 14 Bold')

def fundo3():
    root.configure(background=preto)
    lt1.configure(text='Preto', background=preto)

    lt2= tk.Label(root,text= 'Verde', font= 'Arial 14 Bold')

def fundo4():
    root.configure(background=vermelho)
    lt1.configure(text= 'Vermelho', background= vermelho)

    lt2= tk.Label(root, text= 'Verde', font = 'Arial 14 Bold')


def teste():
    print("Olá Marcos")
def teste3():
    print(" Python")
def teste2():
    print("Olá meu amigo")



root.wm_resizable(width=False, height=False)

button1 = tk.Button(root, text="Azul",font =" Time 10 bold", command=fundo1)
button1.place(width=90, height=50,x=185, y=100,)


button2 = tk.Button(root, text="Verde", font="Time 10 bold", command=fundo2)
button2.place(width=90, height=50,x=185, y=150)

button3 = tk.Button(root, text="Preto", font="Time 10 bold", command=fundo3)
button3.place(width=90, height=50,x=90 , y=150)



button5 = tk.Button (root, text="Vermelho", font="Time 10 bold",command=fundo4)
button5.place(width=90, height=50,x=90,y=100)



root.mainloop()






