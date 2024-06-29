from PIL import Image


def cargar_imagen(ruta):
    return Image.open(ruta).convert('L')


def obtencionPorcentajes(imagen1, imagen2) -> int:
    similitud = 0
    for x in range(imagen1.width):
        for y in range(imagen1.height):
            if imagen1.getpixel((x, y)) == imagen2.getpixel((x, y)):
                similitud += 1
    return (similitud/400)*100  # Devuelve 100 si todas los píxeles son iguales

# C:\Materias\Programas_Lenguaje_Horacio

# Carga la imagen de prueba
prueba=int(input("Dame la imagen de prueba "))
imagen_prueba = cargar_imagen(f'C:\\Materias\\Programas_Lenguaje_Horacio\\Programas1_Perceptron\\NUMEROS\\{prueba}.bmp')

# Cargar y comparar las imágenes de referencia
resultados_similitud = {}
for i in range(1, 101):
    imagen_referencia = cargar_imagen(f'C:\\Materias\\Programas_Lenguaje_Horacio\\Programas1_Perceptron\\NUMEROS\\{i}.bmp')
    if imagen_referencia.size != imagen_prueba.size:
        imagen_referencia = imagen_referencia.resize(imagen_prueba.size)
    similitud = obtencionPorcentajes(imagen_prueba, imagen_referencia)
    resultados_similitud[i] = similitud

# Determinar cuál imagen de referencia es más similar
numero_mas_parecido = max(resultados_similitud, key=resultados_similitud.get)
similitud_max = resultados_similitud[numero_mas_parecido]

if similitud_max == 0:
    print("No se encontró un número parecido.")
else:
    print("Se encontro una concordancia en la imagen", numero_mas_parecido)
    if 1 <= numero_mas_parecido <= 10:
        resultado_final = 0
    elif 11 <= numero_mas_parecido <= 20:
        resultado_final = 1
    elif 21 <= numero_mas_parecido <= 30:
        resultado_final = 2
    elif 31 <= numero_mas_parecido <= 40:
        resultado_final = 3
    elif 41 <= numero_mas_parecido <= 50:
        resultado_final = 4
    elif 51 <= numero_mas_parecido <= 60:
        resultado_final = 5
    elif 61 <= numero_mas_parecido <= 70:
        resultado_final = 6
    elif 71 <= numero_mas_parecido <= 80:
        resultado_final = 7
    elif 81 <= numero_mas_parecido <= 90:
        resultado_final = 8
    elif 91 <= numero_mas_parecido <= 100:
        resultado_final = 9
    print(f"El número es: {resultado_final}")

print(resultados_similitud)

clave_segundo_mayor = sorted(resultados_similitud, key=resultados_similitud.get, reverse=True)[1]
valor_asociado = resultados_similitud[clave_segundo_mayor]
print(f'El indice {clave_segundo_mayor} tiene la mayor similitud con {valor_asociado}')