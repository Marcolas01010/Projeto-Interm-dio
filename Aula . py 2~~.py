import tkinter as tk
root = tk.Tk()

azul = "#1003ff"
verde = "#03ff21"

root.title("Sharkcoders")
root.geometry("500x300+200+200")
root.configure(background=verde)


def teste():
    print("Olá Marcos")
def teste3():
    print(" Python")
def teste2():
    print("Olá meu amigo")



root.wm_resizable(width=False, height=False)

button1 = tk.Button(root, text="Click Me",font =" Time 10 bold", command=teste)
button1.place(x=200, y=100,)


button2 = tk.Button(root, text=" Don't Click me", font = "Time 10 bold", command= teste2)
button2.place(x=185, y=200)


lb1 = tk.Label(root, text="Label 1")
lb1.place(width=70,height=20,x=200,y=50)

lb2 = tk.Label(root ,  text = "Label 2")
lb2.place(width=70,height=20,x=200, y=150)




root.mainloop()
