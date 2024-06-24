import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def apply_kernel(image_path):
    # Leer la imagen
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Definir el kernel (filtro)
    kernel = np.array([[0, -1, 0], 
                       [-1, 5,-1], 
                       [0, -1, 0]])

    # Aplicar el filtro a la imagen
    filtered_image = cv2.filter2D(image_rgb, -1, kernel)

    # Convertir las imágenes a formato PIL para mostrarlas en Tkinter
    original_image_pil = Image.fromarray(image_rgb)
    filtered_image_pil = Image.fromarray(filtered_image)

    return original_image_pil, filtered_image_pil

def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image_pil, filtered_image_pil = apply_kernel(file_path)

        # Mostrar las imágenes en la interfaz
        original_image_tk = ImageTk.PhotoImage(original_image_pil)
        filtered_image_tk = ImageTk.PhotoImage(filtered_image_pil)

        original_label.config(image=original_image_tk)
        original_label.image = original_image_tk
        filtered_label.config(image=filtered_image_tk)
        filtered_label.image = filtered_image_tk

# Configurar la ventana principal
root = tk.Tk()
root.title("Aplicación de Kernel en Imágenes")

# Crear botones y etiquetas para las imágenes
open_button = tk.Button(root, text="Abrir Imagen", command=open_image)
open_button.pack()

original_label = tk.Label(root)
original_label.pack(side="left", padx=10, pady=10)

filtered_label = tk.Label(root)
filtered_label.pack(side="right", padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
