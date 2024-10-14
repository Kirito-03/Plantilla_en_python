from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def planti3():
    # Ventana principal
    informe = tk.Tk()
    informe.title("Informe")
    informe.iconbitmap("Img/logo.ico")
    informe.geometry("960x650")
    informe.grid_rowconfigure(0, weight=10)