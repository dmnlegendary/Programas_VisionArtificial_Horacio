from PIL import Image
import matplotlib.pyplot as plt

def plot_rgb_histogram(image_path):
    # Abrir la imagen
    img = Image.open(image_path)
    
    # Convertir la imagen a RGB si no está en ese modo
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Obtener los datos de la imagen
    pixels = list(img.getdata())
    
    # Inicializar listas para cada canal RGB
    reds = []
    greens = []
    blues = []
    
    # Recorrer todos los píxeles para separar los canales
    for r, g, b in pixels:
        reds.append(r)
        greens.append(g)
        blues.append(b)
    
    # Crear la figura y los ejes para el histograma
    plt.figure(figsize=(10, 6))
    
    # Crear el histograma para cada canal RGB
    plt.hist(reds, bins=256, color='red', alpha=0.5, label='Red')
    plt.hist(greens, bins=256, color='green', alpha=0.5, label='Green')
    plt.hist(blues, bins=256, color='blue', alpha=0.5, label='Blue')
    
    # Añadir título y etiquetas
    plt.title('Histograma de Colores RGB')
    plt.xlabel('Valor de Intensidad')
    plt.ylabel('Frecuencia')
    
    # Añadir leyenda
    plt.legend()
    
    # Mostrar el histograma
    plt.show()

# Ejemplo de uso
image_path = 'arbol.png'
plot_rgb_histogram(image_path)
