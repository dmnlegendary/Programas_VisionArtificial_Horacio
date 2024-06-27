import random
from PIL import Image

def imread(file_path):
    try:
        img = Image.open(file_path)
        return img
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {file_path}")
        return None
    except Exception as e:
        print(f"Error al leer la imagen: {e}")
        return None

def extraer_canales_RGB(img):
    img = img.convert("RGB")
    width, height = img.size
    pixels = list(img.getdata())
    
    channels_r = bytearray()
    channels_g = bytearray()
    channels_b = bytearray()
    
    for r, g, b in pixels:
        channels_r.append(r)
        channels_g.append(g)
        channels_b.append(b)
    
    return channels_r, channels_g, channels_b, width, height

def combinar_canales_RGB(channel_r, channel_g, channel_b, width, height):
    img = Image.new("RGB", (width, height))
    pixels = []
    
    for r, g, b in zip(channel_r, channel_g, channel_b):
        pixels.append((r, g, b))
    
    img.putdata(pixels)
    return img

def matriz_probabilidades(matriz, canal, unique):
    for i in range(len(canal) - 1):
        fila = unique.index(canal[i])
        columna = unique.index(canal[i + 1])
        matriz[fila][columna] += 1
    return matriz

def matriz_sumatoria(matriz, matrizSumatoria):
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
            if matriz[i][j] != 0:
                matrizSumatoria[i][j] += suma
    return matrizSumatoria

def crear_matriz_unica(valores_unicos):
    n = len(valores_unicos)
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return matriz

def generarNuevosCanales(matrizSumatoria, nuevoCanal, tamaño, unique):
    aleatorio = random.randint(0, max(matrizSumatoria[0]))
    col = 0
    for i in range(tamaño):
        aleatorio = random.randint(0, max(matrizSumatoria[col]))
        for j in range(len(matrizSumatoria[0])):
            if aleatorio <= matrizSumatoria[col][j]:
                nuevoCanal.append(unique[j])
                col = j
                break
    return nuevoCanal

imagen = "Federal.jpg"
image = imread(imagen)

if image is not None:
    print("Imagen leída correctamente")
else:
    print("Error al leer la imagen")

channels_r, channels_g, channels_b, width, height = extraer_canales_RGB(image)

unique_r = list(set(channels_r))
unique_g = list(set(channels_g))
unique_b = list(set(channels_b))

matriz_r = crear_matriz_unica(unique_r)
matriz_g = crear_matriz_unica(unique_g)
matriz_b = crear_matriz_unica(unique_b)

matriz_sumatoria_r = crear_matriz_unica(unique_r)
matriz_sumatoria_g = crear_matriz_unica(unique_g)
matriz_sumatoria_b = crear_matriz_unica(unique_b)

matriz_r = matriz_probabilidades(matriz_r, channels_r, unique_r)
matriz_g = matriz_probabilidades(matriz_g, channels_g, unique_g)
matriz_b = matriz_probabilidades(matriz_b, channels_b, unique_b)

matriz_sumatoria_r = matriz_sumatoria(matriz_r, matriz_sumatoria_r)
matriz_sumatoria_g = matriz_sumatoria(matriz_g, matriz_sumatoria_g)
matriz_sumatoria_b = matriz_sumatoria(matriz_b, matriz_sumatoria_b)

new_channels_r = bytearray()
new_channels_g = bytearray()
new_channels_b = bytearray()

new_channels_r = generarNuevosCanales(matriz_sumatoria_r, new_channels_r, len(channels_r), unique_r)
new_channels_g = generarNuevosCanales(matriz_sumatoria_g, new_channels_g, len(channels_g), unique_g)
new_channels_b = generarNuevosCanales(matriz_sumatoria_b, new_channels_b, len(channels_b), unique_b)

'''
print(len(new_channels_r))
print(len(new_channels_g))
print(len(new_channels_b))
'''

new_image = combinar_canales_RGB(new_channels_r, new_channels_g, new_channels_b, width, height)
new_image.save("NuevaImagen.png")