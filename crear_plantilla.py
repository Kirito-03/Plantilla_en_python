from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate #pip install docxtpl
from PIL import Image, ImageTk #pip install pillow  
import tkinter as tk

inicio = tk.Tk()
inicio.title("Frame con Tamaño Fijo con Grid")
inicio.geometry("800x500")
inicio.grid_rowconfigure(0, weight=1)
inicio.resizable(False,False)

imagen_fondo = Image.open("Img/fondo.png")
imagen_fondo = imagen_fondo.resize((500, 500), Image.LANCZOS)  
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

label_fondo = tk.Label(inicio, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=0.625, relheight=1) 

frame = tk.Frame(inicio, bg="lightblue", width=200, height=500) 
frame.pack(side="right", padx=0, pady=0, fill="y")

label = tk.Label(frame, text="  BIENVENIDOS A LA CREACIÓN DE PLANTILLAS KIRITO XD  ", bg="lightblue")
label.pack(padx=10, pady=10)

escg_plantilla=tk.Label(frame,text="¿¿QUE PLANTILLA DESEA ESCOGER??",bg="lightblue")
escg_plantilla.pack()

tipos = ["carta", "presentacion", "diapositiva", "noseda", "xd"]
tp=ttk.Combobox(frame,values=tipos,state="readonly")
tp.set("elige una plantilla")
tp.pack(padx= 5,pady= 5)

#------------------------------------------
def ventana_plantilla():
    if tp.get() == "carta":
        inicio.destroy()
        plant1 = tk.Tk()
        plant1.geometry("600x600")
        plant1.iconbitmap("./Img/Nobara.ico")
        plant1.title("carta")
        
        def plantll1():
            texto=txt1.get()
            plantilla = DocxTemplate("./Doc/plantilla.docx")
            contexto = {"nombre": texto}  
            plantilla.render(contexto)
            plantilla.save(f"{texto}.docx")
            print(f"Documento guardado como {texto}") 
        
        frmcarta=tk.Frame(plant1,width=600,height=600)
        la=Label(frmcarta,text='ingrese sus datos bbe').pack()
        txt1=Entry(frmcarta,width=10)
        txt1.pack()
        bt1=Button(frmcarta,text='presiona bb',command=plantll1).pack()
        
        frmcarta.pack()
        plant1.mainloop()   
#------------------------------------------

iniciar=tk.Button(frame,text="iniciar",command=ventana_plantilla)
iniciar.pack()

inicio.grid_columnconfigure(1, weight=0) 
inicio.mainloop()


