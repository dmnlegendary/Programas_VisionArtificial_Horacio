from PIL import Image
import tkinter

# Cargar la imagen
image = Image.open('LEGO_logo.jpg')

# Garantizar que la imagen trabaje con RGB
image = image.convert('RGB')

# Definir el rango de colores RGB
lower_red = (0,0,0) # (227,168,0),(255,255,0)   
upper_red = (255,0,0)

# Crear una nueva imagen con el tamaño de la original
result = Image.new('RGB', image.size)

# Iterar en cada pixel de la imagen
for x in range(image.width):
    for y in range(image.height):
        r, g, b = image.getpixel((x, y))
        if lower_red[0] <= r <= upper_red[0] and lower_red[1] <= g <= upper_red[1] and lower_red[2] <= b <= upper_red[2]:
            result.putpixel((x, y), (r, g, b))
        else:
            result.putpixel((x, y), (0, 0, 0))
            
# Histogramas para colores


# Mostrar imagen original y modificada
image.show('Imagen Original')
result.show('Resultado')
