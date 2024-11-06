from customtkinter import *
from tkinter import ttk, filedialog, messagebox
from docxtpl import DocxTemplate
from PIL import Image  
import tkinter as tk
import contrato 
from memorando import planti2
import informe
import acta_reunion

def principal():
    set_appearance_mode("dark")
    set_default_color_theme("blue")
    
    inicio = CTk()
    inicio.title("Creación de Plantillas")
    inicio.iconbitmap("Img/logo.ico")

    def centrar_ventana():
        ancho_ventana = 900 
        alto_ventana = 600
        x_ventana = inicio.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = inicio.winfo_screenheight() // 2 - alto_ventana // 2 - 45 
        inicio.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x_ventana, y_ventana))

    inicio.resizable(False, False)

  
    color_fondo_principal = "#00415D"  # Azul oscuro
    color_titulo = "white"           # Azul brillante
    color_subtitulo = "#80CFFA"        # Azul claro
    color_boton = "#00729D"            # Azul intenso para el botón
    color_combo = "#3D5A6D"            # Azul grisáceo

    frame_izquierdo = CTkFrame(inicio, width=400, height=600, fg_color="white")
    frame_izquierdo.pack(side="left", padx=0, pady=0, fill="y")
    
    frame_centrar = CTkFrame(frame_izquierdo, width=200, height=300, fg_color=color_fondo_principal)  
    frame_centrar.pack(side="top", padx=10, pady=10, fill="both", expand=True)
    
    frame_derecho = CTkFrame(inicio, width=500, height=600, fg_color="transparent")
    frame_derecho.pack(side="right", padx=0, pady=0, fill="both", expand=True)

    try:
        img = Image.open("Img/fondo2.jpeg")
        img_resized = img.resize((600, 600), Image.Resampling.LANCZOS)
        fondo = CTkImage(light_image=img_resized, size=(600, 600))
        label_fondo = CTkLabel(frame_derecho, image=fondo, text="")
        label_fondo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    contenedor = CTkFrame(frame_centrar, fg_color="transparent")
    contenedor.grid(row=2, column=2, sticky="nsew", padx=0, pady=100)
    
    try:
        img_logo = Image.open("Img/logo.ico")
        img_resized = img_logo.resize((180, 180), Image.Resampling.LANCZOS)
        fondologo = CTkImage(light_image=img_resized, size=(180, 180))
        label_fondologo = CTkLabel(contenedor, image=fondologo, text="")
        label_fondologo.pack(padx=10, pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    label_titulo = CTkLabel(contenedor, text="Bienvenido a La Automatización", text_color=color_titulo, font=("Tahoma", 30, "bold"))
    label_titulo.pack(padx=20, pady=0)
    
    label_titulo2 = CTkLabel(contenedor, text="De Plantillas DSI", text_color=color_titulo, font=("Tahoma", 30, "bold"))
    label_titulo2.pack(padx=20, pady=0)

    escg_plantilla = CTkLabel(contenedor, text="¿Qué plantilla desea escoger?", text_color=color_subtitulo, font=("Tahoma", 20,))
    escg_plantilla.pack(padx=10, pady=10)

    documentos = [ "Memorando", "Informe", "Acta de reunión", "Carta de presentación"]
    tipos = CTkComboBox(contenedor, values=documentos, state="readonly", font=("Thoma", 12), fg_color=color_combo)
    tipos.set("Elige una plantilla")
    tipos.pack(padx=15, pady=15, fill="x")

    def regresar_a_inicio():
        inicio.deiconify()
        centrar_ventana()

    def elegir_plantillas():
        seleccion = tipos.get()
        if seleccion == "Contrato de trabajo":
            inicio.withdraw()
            return contrato.planti1(regresar_a_inicio)
        elif seleccion == "Memorando":
            inicio.withdraw()
            return planti2()
        elif seleccion == "Informe":
            inicio.withdraw()
            return informe.planti3(regresar_a_inicio)
        elif seleccion == "Acta de reunión":
            inicio.withdraw()
            return acta_reunion.planti4(regresar_a_inicio)
        else:
            messagebox.showinfo("Aviso", "No seleccionó ninguna plantilla")

    

    iniciar = CTkButton(contenedor, text="Iniciar", command=elegir_plantillas, corner_radius=10, fg_color=color_boton, text_color="white", font=("Verdana", 12, "bold"))
    iniciar.pack(padx=15, pady=20)

    centrar_ventana()
    inicio.mainloop()

if __name__ == "__main__":
    principal()
