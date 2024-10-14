from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def planti4():
    # Ventana principal
    acta = tk.Tk()
    acta.title("Acta de Reunion")
    acta.iconbitmap("Img/logo.ico")
    acta.geometry("960x650")
    acta.grid_rowconfigure(0, weight=10)

