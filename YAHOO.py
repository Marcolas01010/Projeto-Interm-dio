import tkinter as tk
root = tk.Tk()

root.title("Sharkcoders")
root.geometry("500x300+200+200")
root.wm_resizable(width=False, height=False)



button1 = tk.Button(root, text="X" , font= 'Time 10 Bold')
button1.grid(row=0 // 3, column=0 //3)