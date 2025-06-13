import tkinter
from tkinter import *
from tkinter import ttk

# Janela principal
tela1 = Tk()
tela1.title("Dados de Modelos de Hypercarros.com.pt🚗")
tela1.geometry('550x580+350+0')
tela1.wm_resizable(width=False, height=False)

# Cores
lb0_color = "#0F729A"
tela_color = "#BCBAB5"

# Função de pesquisa
def pesquisar():
    modelo = comb_modelo.get()
    pais = comb_pais.get()

    # Limpa texto anterior
    lb_resultado.config(text="")

    if modelo == "" or pais == "":
        lb_resultado.config(text="⚠️ Escolhe um modelo e um país!")
        return

    try:
        # Abre o ficheiro com o nome do modelo
        with open(modelo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

            # Junta as 5 primeiras linhas como definições
            definicoes = "".join(linhas[0:5])

            # Mapa de países para índice da linha de preço
            paises_linhas = {
                "Portugal": 5,
                "Alemanha": 6,
                "França": 7,
                "Reino Unido": 8,
                "Brasil": 9,
                "Estados Unidos": 10,
                "Emirados Árabes Unidos": 11
            }

            # Verifica e exibe o preço
            if pais in paises_linhas and paises_linhas[pais] < len(linhas):
                preco = linhas[paises_linhas[pais]].strip()
                texto_final = (
                    f"📋 Definições do {modelo}:\n{definicoes}\n"
                    f"$ Preço em {pais}: {preco}"
                )
                lb_resultado.config(text=texto_final)
            else:
                lb_resultado.config(text="❌ País não encontrado no ficheiro.")

    except FileNotFoundError:
        lb_resultado.config(text=f"❌ Ficheiro do modelo '{modelo}' não encontrado.")

# Atualiza lista de modelos quando a marca muda
def atualizar_eventos(event):
    marca_selecionada = comb_marca.get()
    modelos = marcas_modelos.get(marca_selecionada, [])
    comb_modelo['values'] = modelos
    comb_modelo.set('')

# Cabeçalhos
tkinter.Label(tela1, text="Dados de Modelos de Hypercarros🚗", font="Verdana", bg=lb0_color)\
    .place(width=580, height=100, x=0, y=0)

# Fundo
fundo = tkinter.Label(tela1, bg=tela_color)
fundo.place(width=560, height=550, x=0, y=100)

# Dicionário de marcas e modelos
marcas_modelos = {
    "Lamborghini": ["Aventador", "Huracan", "Gallardo", "Revuelto", "Urus"],
    "Mercedes": ["AMG GT", "S63", "G63", "Project One"],
    "Bmw": ["M3", "M4", "i8", "Z4"],
    "Mclaren": ["P1", "720S", "600LT", "F1"],
    "Ferrari": ["LaFerrari", "488 Pista", "F40", "Enzo Ferrari"]
}

# Labels e Comboboxes
Label(tela1, text="Marca", font="Verdana").place(width=100, height=30, x=30, y=150)
comb_marca = ttk.Combobox(tela1, font='Time 12 bold', justify=CENTER)
comb_marca['values'] = list(marcas_modelos.keys())
comb_marca.bind("<<ComboboxSelected>>", atualizar_eventos)
comb_marca.place(width=122, height=35, x=135, y=150)

Label(tela1, text='Modelo', font="Verdana").place(width=100, height=30, x=275, y=150)
comb_modelo = ttk.Combobox(tela1, font='Verdana')
comb_modelo.place(width=148, height=35, x=385, y=150)

Label(tela1, text='País', font='Verdana').place(width=100, height=30, x=25, y=275)
comb_pais = ttk.Combobox(tela1, font='Verdana')
comb_pais['values'] = [
    "Portugal", "Alemanha", "França", "Reino Unido",
    "Brasil", "Estados Unidos", "Emirados Árabes Unidos"
]
comb_pais.place(width=235, height=35, x=135, y=275)

# Botão de pesquisa
btn_pesquisar = Button(tela1, text="Pesquisar Preço", font="Verdana", command=pesquisar)
btn_pesquisar.place(width=200, height=40, x=175, y=330)

# Label de resultado
lb_resultado = Label(
    tela1,
    text="",
    font="Verdana 10",
    bg="white",
    fg="black",
    justify=LEFT,
    anchor=NW,
    wraplength=480
)
lb_resultado.place(width=500, height=180, x=25, y=380)

# Inicia a aplicação
tela1.mainloop()
