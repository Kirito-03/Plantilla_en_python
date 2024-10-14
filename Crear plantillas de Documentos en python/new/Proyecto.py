from tkinter import *
from tkinter import ttk
from moviepy.editor import VideoFileClip
from moviepy.video.fx import resize
from PIL import Image, ImageTk  # Asegúrate de que esta línea esté presente

inicio = Tk()

# -------------------------------
def new():
    inicio.destroy()
    ventana = Tk()
    ventana.title("miku chichona")
    ventana.iconbitmap("../Img/Nobara.ico")
    ventana.config(bg="white")
    ventana.geometry("600x600")

    def plantillas():
        if combo.get() == "carta":
            ventana.destroy()
            plant1 = Tk()
            plant1.title("carta")
            plant1.iconbitmap("../Img/Nobara.ico")
            plant1.geometry("600x600")
            plant1.mainloop()
        elif combo.get() == "presentacion":
            ventana.destroy()
            plant2 = Tk()
            plant2.title("presentacion")
            plant2.iconbitmap("../Img/Nobara.ico")
            plant2.geometry("600x600")
            plant2.mainloop()

    frame = Frame(ventana, width=600, height=600, bg="blue")
    frame.pack()

    texto = Label(frame, text="que plantilla desea sacar")
    texto.grid()

    lista = ["carta", " presentacion", "diapositiva", "noseda", "xd"]
    combo = ttk.Combobox(ventana, values=lista, state="readonly")
    combo.set("tipo de plantilla")
    combo.pack(padx=5, pady=5)

    nom = Label(ventana, text="nombres")
    nom.pack(padx=5, pady=5)

    bt = Button(ventana, text="guardar", command=plantillas).pack()

    cuadro = Entry(ventana, width=60)
    cuadro.pack()

    menus = Menu(ventana)
    men = Menu(menus)
    men.add_command(label="guardar")
    men.add_command(label="salir")
    men.add_command(label="eliminar")
    menus.add_cascade(label="ayuda", menu=men)
    ventana.configure(menu=menus)

# ------------------------------------------
def reproducir_video():
    # Crear una nueva ventana para reproducir el video
    ventana_video = Toplevel()
    ventana_video.title("Reproducir Video con Tkinter y MoviePy")
    ventana_video.geometry("640x480")

    # Cargar el video usando MoviePy
    video_clip = VideoFileClip("./vd.mp4")

    # Redimensionar el video si es necesario
    video_clip = video_clip.fx(resize.resize, height=480)  # Ajusta la altura según lo necesario

    # Reproducir el video
    video_clip.preview()

# ------------------------------------------


inicio.title("miku chichona")
inicio.iconbitmap("../Img/Nobara.ico")
inicio.config(bg="white")
inicio.geometry("600x600")

# Asegúrate de que "miku.png" esté en el mismo directorio o proporciona la ruta completa
imagen_fondo = Image.open("../Img/miku.png")
imagen_fondo = imagen_fondo.resize((600, 600), Image.LANCZOS)  # Utiliza Image.LANCZOS para redimensionar
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

label_fondo = Label(inicio, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

label_texto = Label(inicio, text="bienvenido a la creacion de plantillas", fg="green", bg="white", font=("Arial", 20))
label_texto.pack(pady=50)

boton = Button(inicio, text="iniciar", command=new, font=("arial", 10))
boton.pack()

boton_video = Button(inicio, text="video", command=reproducir_video, font=("arial", 10))
boton_video.pack()

inicio.mainloop()
