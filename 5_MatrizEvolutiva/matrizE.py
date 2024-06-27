import random

def imread(file_path):
    try:
        with open(file_path, 'rb') as f:
            img_data = f.read()
            return img_data
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {file_path}")
        return None
    except Exception as e:
        print(f"Error al leer la imagen: {e}")
        return None

def extraer_canales_RGB(image_data):
    #Extraer la data de la imagen
    header = image_data[:54]
    width = int.from_bytes(header[18:22], 'little')
    height = int.from_bytes(header[22:26], 'little')
    pixel_data = image_data[54:]
    
    row_padded = (width * 3 + 3) & ~3
    channels_r = bytearray()
    channels_g = bytearray()
    channels_b = bytearray()
    
    for y in range(height):
        for x in range(width):
            offset = y * row_padded + x * 3
            b = pixel_data[offset]
            g = pixel_data[offset + 1]
            r = pixel_data[offset + 2]
            channels_r.append(r)
            channels_g.append(g)
            channels_b.append(b)
    
    return header, channels_r, channels_g, channels_b, width, height

def combinar_canales_RGB(header, channel_r, channel_g, channel_b, width, height):
    row_padded = (width * 3 + 3) & ~3
    combined_image_data = bytearray()
    
    for y in range(height):
        for x in range(width):
            i = y * width + x
            r = channel_r[i]
            g = channel_g[i]
            b = channel_b[i]
            combined_image_data.append(b)
            combined_image_data.append(g)
            combined_image_data.append(r)
        
        padding = row_padded - width * 3
        for _ in range(padding):
            combined_image_data.append(0)
    
    return header + combined_image_data

def matriz_probabilidades(matriz, canal, unique):
    for i in range(len(canal) - 1):
        #Obtener el indice de la fila, donde la fila es el valor actual y la columna es el siguiente valor
        fila = unique.index(canal[i])
        columna = unique.index(canal[i + 1])
        matriz[fila][columna] += 1
    return matriz

def matriz_sumatoria(matriz, matrizSumatoria):
    #Sumar todos los valores de una fila
    #ir iterando por cada fila
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
            if matriz[i][j] != 0:
                matrizSumatoria[i][j] += suma
    return matrizSumatoria


def crear_matriz_unica(valores_unicos):
    n = len(valores_unicos)
    # Crear una matriz nxn con ceros
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    return matriz




imagen = "imagen3.bmp"
image_data = imread(imagen)

if image_data is not None:
    print("Imagen leída correctamente")
else:
    print("Error al leer la imagen")

header, channels_r, channels_g, channels_b, width, height = extraer_canales_RGB(image_data)

#obtener los pixles unicos de cada canal   
unique_r = set(channels_r)
unique_g = set(channels_g)
unique_b = set(channels_b)

unique_r = list(unique_r)
unique_g = list(unique_g)
unique_b = list(unique_b)

# Generar una matriz nxn con los píxeles únicos del canal rojo
matriz_r = crear_matriz_unica(unique_r)
matriz_g = crear_matriz_unica(unique_g)
matriz_b = crear_matriz_unica(unique_b)

matriz_sumatoria_r = crear_matriz_unica(unique_r)
matriz_sumatoria_g = crear_matriz_unica(unique_g)
matriz_sumatoria_b = crear_matriz_unica(unique_b)

# Rellenar la matriz con las probabilidades de transición
matriz_r = matriz_probabilidades(matriz_r, channels_r, unique_r)
matriz_g = matriz_probabilidades(matriz_g, channels_g, unique_g)
matriz_b = matriz_probabilidades(matriz_b, channels_b, unique_b)

#Sumar las probabilidades de transición
matriz_sumatoria_r = matriz_sumatoria(matriz_r, matriz_sumatoria_r)
matriz_sumatoria_g = matriz_sumatoria(matriz_g, matriz_sumatoria_g)
matriz_sumatoria_b = matriz_sumatoria(matriz_b, matriz_sumatoria_b)

#Generar nuevos canales a partir de las matrices de sumatoria, donde generaremos un valor aleatorio entre 0 y el valor máximo cada fila, y ese valor se compara con los valores de esa fila preguntado si es menor o igual, si es menor o igual se toma ese valor, si no se sigue con el siguiente valor de la fila hasta encontrar uno que sea menor o igual al valor aleatorio
#después de encontrar el valor se agrega a un nuevo canal y se toma la columna de ese valor y se pasa como fila para seguir con el proceso donde se vuelve a generar un valor aleatorio y se compara con los valores de esa fila hasta rellenar el nuevo canal
new_channels_r = bytearray()
new_channels_g = bytearray()
new_channels_b = bytearray()


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

# Ejemplo de uso
new_channels_r = generarNuevosCanales(matriz_sumatoria_r, new_channels_r, len(channels_r), unique_r)
new_channels_g = generarNuevosCanales(matriz_sumatoria_g, new_channels_g, len(channels_g), unique_g)
new_channels_b = generarNuevosCanales(matriz_sumatoria_b, new_channels_b, len(channels_b), unique_b)

print(len(new_channels_r))
print(len(new_channels_g))
print(len(new_channels_b))


new_image_data = combinar_canales_RGB(header, new_channels_r, new_channels_g, new_channels_b, width, height)

with open("nueva_imagen.bmp", "wb") as f:
    f.write(new_image_data)
