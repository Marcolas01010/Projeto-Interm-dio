import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("Jogo do Galo")
root.geometry("500x500+400+100")

jogador_atual = 'X'

jogador_sec = 'O'

board = []

for i in range(9):
    board.append('')

buttons = []
for i in range(9):
    button = tk.Button(root, text='', font=('normal', 40), width=5, height=2, command=lambda i=i: clica_button(i))
    button.grid(row=i // 3, column=i % 3)


def reset():
    print("a")


def verifica_vencedor():
    print("aaaa")


def clica_button(index):
    global jogador_atual, board, buttons
    if board[index] == '':
        board[index] = jogador_atual
        buttons[index].config(text=jogador_atual)
        if verifica_vencedor():
            messagebox.showinfo("Fim de Jogo", f"Jogador {jogador_atual} venceu!")
            reset()
        elif '' not in board:
            messagebox.showinfo("Fim de jogo", "Empate!!")
            reset()
        else:
            if jogador_atual == 'X':
                jogador_atual = 'O'
    else:
        jogador_atual = 'X'


for i in range(9):
    button = tk.Button(root, text='', font=('normal', 40), width=5, height=2, command=lambda i=i: clica_button(i))
    button.grid(row=i // 3, column=i % 3)

root.mainloop()