from PIL import Image

# Cargar la imagen
image = Image.open('arbol.png')

# Garantizar que la imagen trabaje con RGB
image = image.convert('RGB')

# Definir el rango de colores RGB
color_rgb = (0,128,255)

# Crear una nueva imagen con el tamaño de la original
result = Image.new('RGB', image.size)

# Iterar en cada pixel de la imagen
for x in range(image.width):
    for y in range(image.height):
        r, g, b = image.getpixel((x, y))
        if color_rgb[0] <= r <= color_rgb[0] and color_rgb[1] <= g <= color_rgb[1] and color_rgb[2] <= b <= color_rgb[2]:
            result.putpixel((x, y), (r, g, b))
        else:
            result.putpixel((x, y), (255, 255, 255))

# Mostrar imagen original y modificada
image.show('Imagen Original')
result.show('Resultado')
