import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from docxtpl import DocxTemplate
from tkinter import *

def planti1(): 
    plant1 = tk.Tk()
    plant1.geometry("900x650")
    plant1.iconbitmap("./Img/logo.ico")
    plant1.title("Contrato de Trabajo")

    # Fondo de la nueva ventana
    frame_contrato = tk.Frame(plant1, bg="#1ABC9C", width=600, height=500)
    frame_contrato.pack(fill="both", expand=True)
    
    #-----Menus
    menu1 = Menu(frame_contrato)
    menu1.add_command(label="cerrar", command=plant1.destroy)
    
    

     # ----------------------------------------- CREAR LA PLANTILLA
    def plantll1():
        texto = nom_empresa.get()
        texto2 = ruc_empresa.get()
        texto3= domicilio_empresa.get()
        texto4 = representante.get()
        plantilla = DocxTemplate("./Doc/contrato_de_trabajo.docx")
        contexto = {"empresa": texto, "ruc": texto2,"domicilio": texto3,"representante": texto4}
        plantilla.render(contexto)

        ruta_guardado = filedialog.asksaveasfilename(
            initialdir="/", 
            title="Guardar documento como", 
            defaultextension=".docx",  
            filetypes=[("Documento Word", "*.docx")]
        )

        if ruta_guardado:
            plantilla.save(ruta_guardado)
            print(f"Documento guardado en: {ruta_guardado}")
    # ---------------------------------------- DATOS DE LA PLANTILLA
    label_datos = tk.Label(frame_contrato, text="Ingrese sus datos:", font=("Helvetica", 14, "bold"), bg="#1ABC9C", fg="white")
    label_datos.grid(row=0, column=0)
        #DATOS A RELLENAR
    nombre_label = tk.Label(frame_contrato, text="empresa", bg="#1ABC9C", fg="white", font=("Helvetica", 12))
    nombre_label.grid(row=1, column=0)
    nom_empresa = tk.Entry(frame_contrato, font=("Helvetica", 12))
    nom_empresa.grid(row=2, column=0)
    ruc_label = tk.Label(frame_contrato, text="ruc", bg="#1ABC9C", fg="white", font=("Helvetica", 12))
    ruc_label.grid(row=3, column=0)
    ruc_empresa = tk.Entry(frame_contrato, font=("Helvetica", 12))
    ruc_empresa.grid(row=4, column=0)
        
    domicilio_label = tk.Label(frame_contrato,text="domicilio", bg="#1ABC9C", fg="white", font=("Helvetica", 12))
    domicilio_label.grid(row=5, column=0)
    domicilio_empresa=tk.Entry(frame_contrato, font=("Helvetica", 12))
    domicilio_empresa.grid(row=6, column=0)
        
    representante_label= tk.Label(frame_contrato,text="representante", bg="#1ABC9C", fg="white", font=("Helvetica", 12))
    representante_label.grid(row=7, column=0)
    representante=tk.Entry(frame_contrato, font=("Helvetica", 12))
    representante.grid(row=8, column=0)
        
     # Botón para generar la plantilla
    bt1 = tk.Button(frame_contrato, text="Crear Plantilla", command=plantll1, bg="#E74C3C", fg="white", font=("Helvetica", 12, "bold"), cursor="hand2")
    bt1.grid(row=9, column=0)

    plant1.config(menu=menu1)
    plant1.mainloop()
