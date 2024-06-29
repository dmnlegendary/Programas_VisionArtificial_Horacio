from PIL import Image

# Función para cargar una imagen en formato BMP y convertirla a escala de grises
def cargar_imagen(ruta):
    return Image.open(ruta).convert('L')

# Función para aplanar la matriz de píxeles de una imagen
def aplanar_imagen(imagen):
    return list(imagen.getdata())

# Función de activación (en este caso, la función escalón)
def funcion_activacion(valor):
    return 1 if valor >= 0 else 0

# Función para entrenar el perceptrón
def entrenar_perceptron(imagenes_entrenamiento, etiquetas_entrenamiento, tasa_aprendizaje=0.1, epocas=100):
    num_caracteristicas = len(imagenes_entrenamiento[0])
    pesos = [0] * num_caracteristicas
    umbral = 0

    for epoca in range(epocas):
        for imagen, etiqueta in zip(imagenes_entrenamiento, etiquetas_entrenamiento):
            entrada_neta = sum(pixel * peso for pixel, peso in zip(imagen, pesos)) + umbral
            salida = funcion_activacion(entrada_neta)
            error = etiqueta - salida

            # Actualizar pesos y umbral
            pesos = [peso + tasa_aprendizaje * error * pixel for pixel, peso in zip(imagen, pesos)]
            umbral += tasa_aprendizaje * error

    return pesos, umbral

# Función para realizar la predicción con el perceptrón entrenado
def predecir_perceptron(imagen, pesos, umbral):
    entrada_neta = sum(pixel * peso for pixel, peso in zip(imagen, pesos)) + umbral
    return funcion_activacion(entrada_neta)

# Función principal
def main():
    # Ruta al directorio que contiene las imágenes BMP
    directorio_imagenes = 'C:\\Materias\\Programas_Lenguaje_Horacio\\Programas1_Perceptron\\NUMEROS\\'

    # Cargar las imágenes de entrenamiento comenzando desde 1
    imagenes_entrenamiento = [cargar_imagen(f'{directorio_imagenes}{i}.bmp') for i in range(1, 101)]

    # Aplanar las imágenes de entrenamiento
    imagenes_entrenamiento_aplanadas = [aplanar_imagen(imagen) for imagen in imagenes_entrenamiento]

    # Etiquetas de entrenamiento (ejemplo: 1 si el número es 1, 0 en otros casos)
    etiquetas_entrenamiento = [[1 if (i % 10) == j else 0 for j in range(10)] for i in range(100)]

    # Entrenar el perceptrón para cada número
    perceptrones_entrenados = [entrenar_perceptron(imagenes_entrenamiento_aplanadas, [etiqueta[i] for etiqueta in etiquetas_entrenamiento]) for i in range(10)]

    # Realizar predicción con el perceptrón entrenado para la imagen de prueba
    opcion=int(input("Dame el número de imagen "))
    imagen_prueba = cargar_imagen(f'{directorio_imagenes}{opcion}.bmp')
    imagen_prueba_aplanada = aplanar_imagen(imagen_prueba)
    predicciones = [predecir_perceptron(imagen_prueba_aplanada, pesos, umbral) for pesos, umbral in perceptrones_entrenados]

    # Obtener el índice del número predicho
    indice_prediccion = predicciones.index(1)

    print(f"La imagen de prueba representa el número: {indice_prediccion}")

if __name__ == "__main__":
    main()
