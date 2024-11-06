from customtkinter import *
from docxtpl import DocxTemplate
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, Menu



def planti4(regresar):
    # Ventana principal
    acta = CTk()
    acta.title("Acta de reunión")
    acta.iconbitmap("Img/logo.ico")
    acta.geometry("960x650")
    acta.grid_rowconfigure(0, weight=10)

    frame = CTkFrame(acta, width=500, height=600, fg_color="transparent")
    frame.pack(side="left", padx=0, pady=0, fill="both", expand=True)
    
    set_appearance_mode("light")
    set_default_color_theme("blue")
    
    def centrar_ventana():
        ancho_ventana = 900 
        alto_ventana = 600
        x_ventana = acta.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = acta.winfo_screenheight() // 2 - alto_ventana // 2 - 45 
        acta.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x_ventana, y_ventana))

    acta.resizable(False, False)

    color_fondo_principal = "blue"  # Azul oscuro
    color_titulo = "#00A2E8"           # Azul brillante
    color_subtitulo = "#80CFFA"        # Azul claro
    color_boton = "#00729D"            # Azul intenso para el botón
    color_combo = "#3D5A6D"  # Azul grisáceo
    
    def regresar_inicio():
        acta.withdraw() 
        regresar()
        
    menu1 = Menu(acta)
    filemenu = Menu(menu1, tearoff=0)
    filemenu.add_command(label="ayuda", command=acta.destroy)
    filemenu.add_command(label="Regresar al Inicio", command=regresar_inicio)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=acta.destroy)
    menu1.add_cascade(label="Opciones", menu=filemenu)
    acta.config(menu=menu1)
    
    def regresar_inicio():
        acta.withdraw() 
        regresar()
    
    def crear_campo(texto, fila, columna,mensaje=""):
        etiqueta = CTkLabel(frame, text=texto, text_color="black", font=("tahoma", 14, "bold"))
        etiqueta.grid(row=fila, column=columna, pady=5, padx=10, sticky="e")
        entrada = CTkEntry(frame, font=("tahoma", 12),placeholder_text=mensaje)
        entrada.grid(row=fila, column=columna+1, pady=5, padx=10)
        return entrada
    
    sobre =crear_campo("Sobre:", 0, 0)
    ciudad = crear_campo("Ciudad:", 1, 0)
    dia = crear_campo("Fecha:", 2, 0)
    mes = crear_campo("Mes:", 3, 0)
    año = crear_campo("Año:", 4, 0)
    hora = crear_campo("Hora:", 5, 0)
    lugar_reunion = crear_campo("Lugar:", 6, 0)
    asitente_nombre = crear_campo("Asistente:", 7, 0)
    cargo = crear_campo("Cargo:", 8, 0)
    detallar_Acuerdos = crear_campo("Detallar Acuerdos:", 9, 0)
    acuerdos = crear_campo("Acuerdos:", 10, 0)
    hora_cierre = crear_campo("Hora Cierre:", 11, 0)
    
    def guardar():
        try:
            contexto = {
                "sobre": sobre.get(),
                "ciudad": ciudad.get(),
                "dia": dia.get(),
                "mes": mes.get(),
                "año": año.get(),
                "hora": hora.get(),
                "lugar_reunion": lugar_reunion.get(),
                "nombre_complete": asitente_nombre.get(),
                "cargo": cargo.get(),
                "detallar_Acuerdos": detallar_Acuerdos.get(),
                "acuerdos": acuerdos.get(),
                "hora_cierre": hora_cierre.get(),
            }
            ruta_plantilla = "./Doc/acta_reunion.docx"
            if not os.path.exists(ruta_plantilla):
                messagebox.showerror("Error", f"No se encontró la plantilla en {ruta_plantilla}")
                return

            # Cargar la plantilla y renderizar con los datos ingresados
            plantilla = DocxTemplate(ruta_plantilla)
            plantilla.render(contexto)
            plantilla.save("./Doc/acta_reunion.docx")

            # Guardar el archivo
            ruta_guardado = filedialog.asksaveasfilename(
                initialdir="/",
                title="Guardar documento como",
                defaultextension=".docx",
                filetypes=[("Documento Word", "*.docx")]
            )
            if ruta_guardado:
                plantilla.save(ruta_guardado)
                messagebox.showinfo("Éxito", f"Documento guardado en: {ruta_guardado}")


        except Exception as e:
            messagebox.showerror("Error", f"Error al generar el contrato: {str(e)}")
    def limpiar():
        sobre.delete(0, tk.END)
        ciudad.delete(0, tk.END)
        dia.delete(0, tk.END)
        mes.delete(0, tk.END)
        año.delete(0, tk.END)
        hora.delete(0, tk.END)
        lugar_reunion.delete(0, tk.END)
        asitente_nombre.delete(0, tk.END)
        cargo.delete(0, tk.END)
        detallar_Acuerdos.delete(0, tk.END)
        acuerdos.delete(0, tk.END)
        hora_cierre.delete(0, tk.END)
    
    boton_guardar = CTkButton(frame, text="Guardar", width=100, height=30, fg_color=color_boton, command=guardar)
    boton_guardar.grid(row=12, column=0, pady=10, padx=10, sticky="nsew")

    boton_limpiar = CTkButton(frame, text="Limpiar", width=100, height=30, fg_color=color_boton, command=limpiar)
    boton_limpiar.grid(row=12, column=1, pady=10, padx=10, sticky="nsew")
    
    centrar_ventana()
    acta.mainloop()
if __name__ == "__main__":
    planti4(NONE)

