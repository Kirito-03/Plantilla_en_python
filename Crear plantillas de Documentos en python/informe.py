from customtkinter import *
from docxtpl import DocxTemplate
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, Menu
import json
import os

# Ruta del archivo de historial
HISTORIAL_PATH = "./historial_documentos.json"

def cargar_historial():
    """Cargar historial desde el archivo JSON, devolviendo una lista vacía si el archivo no existe o está vacío."""
    if os.path.exists(HISTORIAL_PATH):
        try:
            with open(HISTORIAL_PATH, 'r') as file:
                historial = json.load(file)
                if isinstance(historial, list):
                    return historial
        except json.JSONDecodeError:
            return []
    return []

def guardar_en_historial(nombre, ruta):
    """Guardar el documento en el historial JSON."""
    if nombre and ruta:  # Verificar que ambos campos no estén vacíos
        historial = cargar_historial()
        historial.append({"nombre": nombre, "ruta": ruta})
        with open(HISTORIAL_PATH, 'w') as file:
            json.dump(historial, file)


def planti3(regresar):
    informe = CTk()
    informe.title("informe")
    informe.iconbitmap("Img/logo.ico")
    informe.geometry("900x600")
    informe.resizable(False, False)
    
    set_appearance_mode("light")
    set_default_color_theme("blue")
    
    def centrar_ventana():
        ancho_ventana = 900 
        alto_ventana = 600
        x_ventana = informe.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = informe.winfo_screenheight() // 2 - alto_ventana // 2 - 45 
        informe.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x_ventana, y_ventana))

    frame = CTkFrame(informe, width=500, height=600, fg_color="transparent")
    frame.pack(side="left", padx=0, pady=0, fill="both", expand=True)
    
    def regresar_inicio():
        informe.withdraw()
        regresar()
    
    menu1 = Menu(informe)
    filemenu = Menu(menu1, tearoff=0)
    filemenu.add_command(label="ayuda", command=informe.destroy)
    filemenu.add_command(label="Regresar al Inicio", command=regresar_inicio)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=informe.destroy)
    menu1.add_cascade(label="Opciones", menu=filemenu)
    informe.config(menu=menu1)
    
    
    def mover_siguiente(event, siguiente_entry):
        siguiente_entry.focus()

    # Crear campos de entrada sin el parámetro `siguiente`
    SOBRE_QUE = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese el tema")
    fechaemision = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese la fecha de emisión")
    nombre_del_destinatario = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese el nombre del destinatario")
    nombre_del_remitente = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese el nombre del remitente")
    asunto = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese el asunto")
    describir_proposito_del_informe = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Describa el propósito del informe")
    fecha_inicio = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese la fecha de inicio")
    fecha_finalizacion = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese la fecha de finalización")
    descripcion_de_actividad = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Describa la actividad")
    descripcion_de_observacion = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Describa las observaciones")
    resumen_de_conclusiones = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Resuma las conclusiones")
    nombre_del_responsable = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese el nombre del responsable")
    cargo_responsable = CTkEntry(frame, font=("tahoma", 12), placeholder_text="Ingrese el cargo del responsable")

    # Crear etiquetas y posicionar los campos de entrada en la ventana
    def crear_campo_con_icono(texto, fila, columna, entry, icono):
        etiqueta_icono = CTkLabel(frame, image=icono, text="")  # Coloca el ícono al lado de la etiqueta
        etiqueta_icono.grid(row=fila, column=columna, pady=5, padx=5, sticky="e")
        etiqueta = CTkLabel(frame, text=texto, text_color="black", font=("tahoma", 14, "bold"))
        etiqueta.grid(row=fila, column=columna + 1, pady=5, padx=10, sticky="e")
    
        entry.grid(row=fila, column=columna + 2, pady=5, padx=10)
        
    # global icon_sobre, icon_fecha, icon_destinatario, icon_remitente, icon_asuntoicon_proposito
    # global icon_inicio, icon_final, icon_actividad, icon_observacion, icon_conclusiones, icon_responsable, icon_cargo
    
    # try:
    #     icon_sobre = CTkImage(Image.open("./Img/icon_informe/sobre_que.png").resize((20, 20)))
    #     icon_fecha = CTkImage(Image.open("./Img/icon_informe/fecha_emision.png").resize((20, 20)))
    #     icon_destinatario = CTkImage(Image.open("./Img/icon_informe/nombre.png").resize((20, 20)))
    #     icon_remitente = CTkImage(Image.open("./Img/icon_informe/nombre.png").resize((20, 20)))
    #     icon_asunto = CTkImage(Image.open("./Img/icon_informe/asunto.png").resize((20, 20)))
    #     icon_proposito = CTkImage(Image.open("./Img/icon_informe/descripcion_informe.png").resize((20, 20)))
    #     icon_inicio = CTkImage(Image.open("./Img/icon_informe/fecha_inicio.png").resize((20, 20)))
    #     icon_final = CTkImage(Image.open("./Img/icon_informe/fecha_fin.png").resize((20, 20)))
    #     icon_actividad = CTkImage(Image.open("./Img/icon_informe/actividad.png").resize((20, 20)))
    #     icon_observacion = CTkImage(Image.open("./Img/icon_informe/observaciones.png").resize((20, 20)))
    #     icon_conclusiones = CTkImage(Image.open("./Img/icon_informe/resumen.png").resize((20, 20)))
    #     icon_responsable = CTkImage(Image.open("./Img/icon_informe/nombre.png").resize((20, 20)))
    #     icon_cargo = CTkImage(Image.open("./Img/icon_informe/cargo.png").resize((20, 20)))
    # except FileNotFoundError:
    #     print("No se encontró alguna imagen.")

    # Función para crear campos con icono y etiqueta
    def crear_campo_con_icono(texto, fila, columna, entry):
        etiqueta_icono = CTkLabel(frame, text="")  # Coloca el ícono al lado de la etiqueta
        etiqueta_icono.grid(row=fila, column=columna, pady=5, padx=5, sticky="e")
        etiqueta = CTkLabel(frame, text=texto, text_color="black", font=("tahoma", 14, "bold"))
        etiqueta.grid(row=fila, column=columna + 1, pady=5, padx=10, sticky="e")
        entry.grid(row=fila, column=columna + 2, pady=5, padx=10)

    # Creación de los campos de entrada con iconos
    # crear_campo_con_icono("Sobre que:", 0, 0, SOBRE_QUE, icon_sobre)
    # crear_campo_con_icono("Fecha de emisión:", 1, 0, fechaemision, icon_fecha)
    # crear_campo_con_icono("Nombre del destinatario:", 2, 0, nombre_del_destinatario, icon_destinatario)
    # crear_campo_con_icono("Nombre del remitente:", 3, 0, nombre_del_remitente, icon_remitente)
    # crear_campo_con_icono("Asunto:", 4, 0, asunto, icon_asunto)
    # crear_campo_con_icono("Describir el propósito del informe:", 5, 0, describir_proposito_del_informe, icon_proposito)
    # crear_campo_con_icono("Fecha de inicio:", 6, 0, fecha_inicio, icon_inicio)
    # crear_campo_con_icono("Fecha de finalización:", 7, 0, fecha_finalizacion, icon_final)
    # crear_campo_con_icono("Describir la actividad:", 8, 0, descripcion_de_actividad, icon_actividad)
    # crear_campo_con_icono("Describir las observaciones:", 9, 0, descripcion_de_observacion, icon_observacion)
    # crear_campo_con_icono("Resumen de conclusiones:", 10, 0, resumen_de_conclusiones, icon_conclusiones)
    # crear_campo_con_icono("Nombre del responsable:", 11, 0, nombre_del_responsable, icon_responsable)
    # crear_campo_con_icono("Cargo del responsable:", 12, 0, cargo_responsable, icon_cargo)
    
    crear_campo_con_icono("Sobre que:", 0, 0, SOBRE_QUE)
    crear_campo_con_icono("Fecha de emisión:", 1, 0, fechaemision)
    crear_campo_con_icono("Nombre del destinatario:", 2, 0, nombre_del_destinatario)
    crear_campo_con_icono("Nombre del remitente:", 3, 0, nombre_del_remitente)
    crear_campo_con_icono("Asunto:", 4, 0, asunto)
    crear_campo_con_icono("Describir el propósito del informe:", 5, 0, describir_proposito_del_informe)
    crear_campo_con_icono("Fecha de inicio:", 6, 0, fecha_inicio)
    crear_campo_con_icono("Fecha de finalización:", 7, 0, fecha_finalizacion)
    crear_campo_con_icono("Describir la actividad:", 8, 0, descripcion_de_actividad)
    crear_campo_con_icono("Describir las observaciones:", 9, 0, descripcion_de_observacion)
    crear_campo_con_icono("Resumen de conclusiones:", 10, 0, resumen_de_conclusiones)
    crear_campo_con_icono("Nombre del responsable:", 11, 0, nombre_del_responsable)
    crear_campo_con_icono("Cargo del responsable:", 12, 0, cargo_responsable)

    
    
    # Lista de los campos de entrada en orden para configurar el Enter
    entradas = [
        SOBRE_QUE, fechaemision, nombre_del_destinatario, nombre_del_remitente,
        asunto, describir_proposito_del_informe, fecha_inicio, fecha_finalizacion,
        descripcion_de_actividad, descripcion_de_observacion, resumen_de_conclusiones,
        nombre_del_responsable, cargo_responsable
    ]

    # Vincular cada campo de entrada con el siguiente en la lista
    for i in range(len(entradas) - 1):
        entradas[i].bind("<Return>", lambda event, siguiente=entradas[i + 1]: mover_siguiente(event, siguiente))

    
    # Cargar datos de un documento del historial en los campos de entrada
    def cargar_documento(ruta):
        try:
            plantilla = DocxTemplate(ruta)
            contexto = plantilla.docx.get_context()
            # Asigna los valores de contexto a cada campo
            SOBRE_QUE.insert(0, contexto.get("SOBRE_QUE", ""))
            fechaemision.insert(0, contexto.get("fechaemision", ""))
            nombre_del_destinatario.insert(0, contexto.get("nombre_del_destinatario", ""))
            nombre_del_remitente.insert(0, contexto.get("nombre_del_remitente", ""))
            asunto.insert(0, contexto.get("asunto_del_informe", ""))
            describir_proposito_del_informe.insert(0, contexto.get("describir_proposito_del_informe", ""))
            fecha_inicio.insert(0, contexto.get("fecha_inicio", ""))
            fecha_finalizacion.insert(0, contexto.get("fecha_finalizacion", ""))
            descripcion_de_actividad.insert(0, contexto.get("descripcion_de_actividad", ""))
            descripcion_de_observacion.insert(0, contexto.get("descripcion_de_observacion", ""))
            resumen_de_conclusiones.insert(0, contexto.get("resumen_de_conclusiones", ""))
            nombre_del_responsable.insert(0, contexto.get("nombre_del_responsable", ""))
            cargo_responsable.insert(0, contexto.get("cargo_responsable", ""))
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el documento: {e}")

    # Guardar nuevo informe y agregarlo al historial
    def guardar_informe():
        try:
            contexto = {
                "SOBRE_QUE": SOBRE_QUE.get(),
                "fechaemision": fechaemision.get(),
                "nombre_del_destinatario": nombre_del_destinatario.get(),
                "nombre_del_remitente": nombre_del_remitente.get(),
                "asunto_del_informe": asunto.get(),
                "describir_proposito_del_informe": describir_proposito_del_informe.get(),
                "fecha_inicio": fecha_inicio.get(),
                "fecha_finalizacion": fecha_finalizacion.get(),
                "descripcion_de_actividad": descripcion_de_actividad.get(),
                "descripcion_de_observacion": descripcion_de_observacion.get(),
                "resumen_de_conclusiones": resumen_de_conclusiones.get(),
                "nombre_del_responsable": nombre_del_responsable.get(),
                "cargo_responsable": cargo_responsable.get(),
            }
            plantilla = DocxTemplate("./Doc/Informe.docx")
            plantilla.render(contexto)

            ruta_guardado = filedialog.asksaveasfilename(
                initialdir="/",
                title="Guardar documento como",
                defaultextension=".docx",
                filetypes=[("Documento Word", "*.docx")]
            )
            if ruta_guardado:
                plantilla.save(ruta_guardado)
                guardar_en_historial(contexto["asunto_del_informe"], ruta_guardado)
                messagebox.showinfo("Éxito", f"Documento guardado en: {ruta_guardado}")

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el informe: {e}")
            
    def limpiar_campos():
        SOBRE_QUE.delete(0, tk.END)
        fechaemision.delete(0, tk.END)
        nombre_del_destinatario.delete(0, tk.END)
        nombre_del_remitente.delete(0, tk.END)
        asunto.delete(0, tk.END)
        describir_proposito_del_informe.delete(0, tk.END)
        fecha_inicio.delete(0, tk.END)
        fecha_finalizacion.delete(0, tk.END)
        descripcion_de_actividad.delete(0, tk.END)
        descripcion_de_observacion.delete(0, tk.END)
        resumen_de_conclusiones.delete(0, tk.END)
        nombre_del_responsable.delete(0, tk.END)
        cargo_responsable.delete(0, tk.END)

    # ComboBox para seleccionar un documento del historial
    historial = cargar_historial()
    # Cargar nombres de documentos en el historial solo si contienen la clave "nombre"
    historial_nombres = [item["nombre"] for item in historial if "nombre" in item]
    seleccion_historial = tk.StringVar()
    combo_historial = CTkComboBox(frame, values=historial_nombres, variable=seleccion_historial)
    combo_historial.grid(row=13, column=0, columnspan=2, pady=10)
    
    def cargar_desde_historial():
        seleccion = seleccion_historial.get()
        documento = next((item for item in historial if item["nombre"] == seleccion), None)
        if documento:
            cargar_documento(documento["ruta"])

    boton_cargar_historial = CTkButton(informe, text="Cargar del Historial", command=cargar_desde_historial)
    boton_cargar_historial.pack(pady=5)

    boton_guardar = CTkButton(informe, text="Guardar Informe", command=guardar_informe)
    boton_guardar.pack(pady=10)
    
    boton_limpiar = CTkButton(informe, text="Limpiar Campos", command=limpiar_campos)
    boton_limpiar.pack(pady=10)

    centrar_ventana()
    informe.mainloop()
if __name__ == "__main__":
    planti3(NONE)