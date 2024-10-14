from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate  # pip install docxtpl
from PIL import Image, ImageTk  # pip install pillow  
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from contrato import planti1
from memorando import planti2
from informe import planti3
from acta_reunion import planti4

# Ventana principal
inicio = tk.Tk()
inicio.title("Creación de Plantillas")
inicio.iconbitmap("Img/logo.ico")
inicio.geometry("600x400")
inicio.grid_rowconfigure(0, weight=10)
inicio.resizable(False, False)

# --FONDO
imagen_fondo = Image.open("Img/fondopro.png")
imagen_fondo = imagen_fondo.resize((500, 500), Image.LANCZOS)
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

label_fondo = tk.Label(inicio, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=0.625, relheight=1)
#---logo
logo = Image.open("Img/logo3.png")
logo = logo.resize((80, 80), Image.LANCZOS)
logo_tk = ImageTk.PhotoImage(logo)

label_logo = tk.Label(inicio, image=logo_tk,background="#6996d3")
label_logo.place(x=0, y=0)

# --------------------------FRAME
frame = tk.Frame(inicio, bg="#2C3E50", width=300, height=500)
frame.pack(side="right", padx=0, pady=0, fill="y")

# Estilos personalizados
label_style = {"bg": "#2C3E50", "fg": "white", "font": ("Helvetica", 12)}
titulo_style = {"bg": "#2C3E50", "fg": "white", "font": ("Helvetica", 14, "bold")}

label = tk.Label(frame, text="BIENVENIDOS A LA CREACIÓN DE PLANTILLAS KIRITO XD", **titulo_style, wraplength=250, justify="center")
label.pack(padx=10, pady=20)

escg_plantilla = tk.Label(frame, text="¿Qué plantilla desea escoger?", **label_style)
escg_plantilla.pack(padx=10, pady=10)

# -------------------TIPOS DE PLANTILLA
documentos = [
    "Contrato de trabajo",
    "Memorando", "Informe", "Acta de reunión",
    "Currículum vitae (CV)", "Carta de presentación"
]

tipos = ttk.Combobox(frame, values=documentos, state="readonly", font=("Helvetica", 10))
tipos.set("Elige una plantilla")
tipos.pack(padx=15, pady=15)

def elegir_plantillas():
    if tipos.get() == "Contrato de trabajo":
        inicio.withdraw()
        return planti1()
    elif tipos.get() == "Memorando":
        inicio.withdraw()
        return planti2()
    elif tipos.get() == "Informe":
        inicio.withdraw()
        return planti3()
    elif tipos.get() == "Acta de reunión":
        inicio.withdraw()
        return planti4()
        
    else :
        messagebox.showinfo("Aviso", "NO SELECCIONO NINGUNA PLANTILLA")
# --------------------- BOTÓN INICIAR
iniciar = tk.Button(frame, text="Iniciar", command=elegir_plantillas, bg="blue", fg="white", font=("Helvetica", 12, "bold"), cursor="hand2")
iniciar.pack(padx=15, pady=20)

# Configurar ventana principal
inicio.grid_columnconfigure(1, weight=0)
inicio.mainloop()
