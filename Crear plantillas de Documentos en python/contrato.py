import tkinter as tk
from customtkinter import * #pip install customtkinter
from tkinter import filedialog, messagebox, Menu
from docxtpl import DocxTemplate
from tkcalendar import * #pip install tkcalendar
import os

def planti1(regresar):  # Aceptar la función de callback como argumento
    # Crear ventana principal
    plant1 = CTk()
    plant1.geometry("900x600")
    plant1.iconbitmap("./Img/logo.ico") 
    plant1.title("Contrato de Trabajo")

    def centrar_ventana():
        ancho_ventana = 900 
        alto_ventana = 600
        x_ventana = plant1.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = plant1.winfo_screenheight() // 2 - alto_ventana // 2 - 45 
        plant1.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, x_ventana, y_ventana))   
        
    # Fondo de la nueva ventana
    frame_contrato = CTkFrame(plant1, fg_color="#005C6f", width=600, height=500)
    frame_contrato.pack(fill="both", expand=True)

    # Función para crear campos de texto
    def crear_campo(texto, fila, columna):
        etiqueta = CTkLabel(frame_contrato, text=texto, text_color="black", font=("Fixedsys", 14, "bold"))
        etiqueta.grid(row=fila, column=columna, pady=5, padx=10, sticky="e")
        entrada = CTkEntry(frame_contrato, font=("Helvetica", 12))
        entrada.grid(row=fila, column=columna+1, pady=5, padx=10)

    # Función para regresar al inicio
    def regresar_inicio():
        plant1.withdraw() 
        regresar()


    # Menú 
    menu1 = Menu(plant1)
    filemenu = Menu(menu1, tearoff=0)
    filemenu.add_command(label="ayuda", command=plant1.destroy)
    filemenu.add_command(label="Regresar al Inicio", command=regresar_inicio)
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=plant1.destroy)
    menu1.add_cascade(label="Opciones", menu=filemenu)
    plant1.config(menu=menu1)

    # Función para crear la plantilla con los datos
    def plantll1():
        try:
            # Obtener los valores de los campos
            contexto = {
                "nom_empresa": nom_empresa.get(),
                "ruc_empresa": ruc_empresa.get(),
                "domicilio_empresa": domicilio_empresa.get(),
                "representante": representante.get(),
                "dni_representante": dni_representante.get(),
                "trabajador": nom_trabajador.get(),
                "dni_trabajador": dni_trabajador.get(),
                "domicilio_trabajador": domicilio_trabajador.get(),
                "ciudad": ciudad_empresa.get(),
                "actividad_empresa": actividad_empresa.get(),
                "cargo": cargo.get(),
                "duracion": duracion_contrato.get(),
                "fecha_inicio": fecha_inicio.get(),
                "fecha_fin": fecha_fin.get(),
                "horario_inicio": horario_inicio.get(),
                "horario_fin": horario_fin.get(),
                "remuneracion": remuneracion.get(),
                "fecha_contrato": fecha_contrato.get(),
            }

            # Verificar si la plantilla existe
            ruta_plantilla = "./Doc/contrato_de_trabajo.docx"
            if not os.path.exists(ruta_plantilla):
                messagebox.showerror("Error", f"No se encontró la plantilla en {ruta_plantilla}")
                return

            # Cargar la plantilla y renderizar con los datos ingresados
            plantilla = DocxTemplate(ruta_plantilla)
            plantilla.render(contexto)
            plantilla.save("./Doc/Contrato.docx")

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

    # Título del formulario
    label_datos = CTkLabel(
        frame_contrato, text="Ingrese sus datos:", font=("Comic Sans MS", 16, "bold"),
        text_color="white"
    )
    label_datos.grid(row=0, column=0, pady=10, columnspan=4)

    # Campos para rellenar organizados en dos columnas
    def crear_campo(texto, fila, columna,mensaje=""):
        etiqueta = CTkLabel(frame_contrato, text=texto, text_color="black", font=("Fixedsys", 14, "bold"))
        etiqueta.grid(row=fila, column=columna, pady=5, padx=10, sticky="e")
        entrada = CTkEntry(frame_contrato, font=("Helvetica", 12),placeholder_text=mensaje)
        entrada.grid(row=fila, column=columna+1, pady=5, padx=10)
        return entrada
    def crear_campoData(texto, fila, columna):
        etiqueta1 = CTkLabel(frame_contrato, text=texto, text_color="black", font=("Fixedsys", 14, "bold"))
        etiqueta1.grid(row=fila, column=columna, pady=5, padx=10, sticky="e")
        entrada1 = DateEntry(frame_contrato, font=("Helvetica", 12))
        entrada1.grid(row=fila, column=columna+1, pady=5, padx=10)
        return entrada1
        
        
    # Primera columna
    nom_empresa = crear_campo("Empresa", 1, 0)
    ruc_empresa = crear_campo("RUC", 2, 0)
    domicilio_empresa = crear_campo("Domicilio Empresa", 3, 0)
    representante = crear_campo("Representante", 4, 0)
    dni_representante = crear_campo("DNI Representante", 5, 0)
    nom_trabajador = crear_campo("Trabajador", 6, 0)
    dni_trabajador = crear_campo("DNI Trabajador", 7, 0)
    domicilio_trabajador = crear_campo("Domicilio Trabajador", 8, 0)
    ciudad_empresa = crear_campo("Ciudad", 9, 0)
    # Segunda columna
    actividad_empresa = crear_campo("Actividad Empresa", 1, 2)
    cargo = crear_campo("Cargo", 2, 2)
    duracion_contrato = crear_campo("Duración Contrato (meses)", 3, 2)
    fecha_inicio = crear_campoData("Fecha Inicio", 4, 2)
    fecha_fin = crear_campoData("Fecha Fin", 5, 2)
    horario_inicio = crear_campo("Horario Inicio", 6, 2)
    horario_fin = crear_campo("Horario Fin", 7, 2)
    remuneracion = crear_campo("Remuneración", 8, 2)
    fecha_contrato = crear_campoData("Fecha de Firma", 9, 2)

    def limpiar():
        nom_empresa.delete(0, tk.END)
        ruc_empresa.delete(0, tk.END)
        domicilio_empresa.delete(0, tk.END)
        representante.delete(0, tk.END)
        dni_representante.delete(0, tk.END)
        nom_trabajador.delete(0, tk.END)
        dni_trabajador.delete(0, tk.END)
        domicilio_trabajador.delete(0, tk.END)
        ciudad_empresa.delete(0, tk.END)
        actividad_empresa.delete(0, tk.END)
        cargo.delete(0, tk.END)
        duracion_contrato.delete(0, tk.END)
        fecha_inicio.delete(0, tk.END)
        fecha_fin.delete(0, tk.END)
        horario_inicio.delete(0, tk.END)
        horario_fin.delete(0, tk.END)
        remuneracion.delete(0, tk.END)
        fecha_contrato.delete(0, tk.END)

    # Botón para generar contrato
    btn_generar = CTkButton(
        frame_contrato, text="Generar", font=("Helvetica", 12),
        fg_color="#2980B9", text_color="white", command=plantll1)
    btn_generar.grid(row=11, column=0, columnspan=4, pady=10)

    btn_limpiar = CTkButton(
        frame_contrato, text="Limpiar", font=("Helvetica", 12),
        fg_color="#2980B9", text_color="white", command=limpiar)
    btn_limpiar.grid(row=12, column=0, columnspan=4, pady=10)

    centrar_ventana()
    plant1.mainloop()
if __name__ == "__main__":
    planti1(NONE)
