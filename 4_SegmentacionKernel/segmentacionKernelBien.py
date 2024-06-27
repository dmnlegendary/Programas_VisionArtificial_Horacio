import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps

def apply_kernel(image_path):
    # Leer la imagen
    image = Image.open(image_path)
    image = ImageOps.exif_transpose(image)  # Corregir la orientación usando EXIF

    # Redimensionar la imagen si es más grande que 500x500
    max_size = (500, 500)
    image.thumbnail(max_size)

    image_rgb = image.convert("RGB")
    image_data = image_rgb.load()

    # Kernel de relieve (Emboss)
    '''[[-2, -1, 0], 
              [-1, 1, 1], 
              [0, 1, 2]]'''
              
    '''[[0, -1, 0], 
              [-1, 5, -1], 
              [0, -1, 0]]
'''
    
    '''[[-1, -2, -1], 
              [0,0, 0], 
              [1, 2, 1]] Sobel horizontal'''
              
    kernel = [[-1, -1, -1], 
              [-1,8, -1], 
              [-1, -1,-1]]

    # Obtener las dimensiones de la imagen
    ancho, altura = image_rgb.size

    # Crear una imagen de salida
    filtered_image = Image.new("RGB", (ancho, altura))
    filtered_image_data = filtered_image.load()

    # Aplicar el filtro a la imagen
    for i in range(1, ancho-1):
        for j in range(1, altura-1):
            for c in range(3):  # Para cada canal (R, G, B)
                filtered_value = (
                    kernel[0][0] * image_data[i-1, j-1][c] + kernel[0][1] * image_data[i, j-1][c] + kernel[0][2] * image_data[i+1, j-1][c] +
                    kernel[1][0] * image_data[i-1, j][c] + kernel[1][1] * image_data[i, j][c] + kernel[1][2] * image_data[i+1, j][c] +
                    kernel[2][0] * image_data[i-1, j+1][c] + kernel[2][1] * image_data[i, j+1][c] + kernel[2][2] * image_data[i+1, j+1][c]
                )
                filtered_value = max(0, min(255, filtered_value))  # Asegurarse de que el valor esté entre 0 y 255
                filtered_image_data[i, j] = tuple(
                    filtered_value if k == c else image_data[i, j][k] for k in range(3)
                )

    return image_rgb, filtered_image

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
root.title("Segmentacion por Kernel")
root.geometry("1280x720")
root.config(bg="#FF8040")

# Crear botones y etiquetas para las imágenes
open_button = tk.Button(root, text="Abrir Imagen", bg="#00DDAA", fg="#FFFFFF", font=("Verdana", 16, "bold"), command=open_image)
open_button.pack(side=tk.TOP, padx=40, pady=40)

original_label = tk.Label(root)
original_label.pack(side=tk.LEFT, padx=10, pady=10)

filtered_label = tk.Label(root)
filtered_label.pack(side=tk.RIGHT, padx=10, pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
