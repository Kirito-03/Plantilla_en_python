from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from customtkinter import *

def planti2():
    # Ventana principal
    memorando = CTk()
    memorando.title("Memorando")
    memorando.iconbitmap("Img/logo.ico")
    memorando.geometry("960x650")
    memorando.grid_rowconfigure(0, weight=10)
    
    frame = CTkFrame(memorando, width=500, height=600, fg_color="transparent")
    frame.pack(side="left", padx=0, pady=0, fill="both", expand=True)
    
    def centrar_ventana():
        ancho_ventana = 900 
        alto_ventana = 600
        x_ventana = memorando.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = memorando.winfo_screenheight() // 2 - alto_ventana // 2 - 45 
        memorando.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x_ventana, y_ventana))

    memorando.resizable(False, False)

    color_fondo_principal = "blue"  # Azul oscuro
    color_titulo = "#00A2E8"           # Azul brillante
    color_subtitulo = "#80CFFA"        # Azul claro
    color_boton = "#00729D"            # Azul intenso para el botón
    color_combo = "#3D5A6D"  # Azul grisáceo

    centrar_ventana()
    memorando.mainloop()
