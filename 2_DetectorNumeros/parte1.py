from PIL import Image

# Direcciones de las imagenes a trabajar
imagen_del_numero_original = "C:\\Materias\\Programas_Lenguaje_Horacio\\Programas1_Perceptron\\NUMEROS\\1.bmp"
imagen_del_numero_entrada = "C:\\Materias\\Programas_Lenguaje_Horacio\\Programas1_Perceptron\\NUMEROS\\1.bmp"

# Funcion para comparar las imagenes
def comparar_imagenes(Imagen_Original, Imagen_Entrada):
    # Carga de imagenes al programa
    image1 = Image.open(Imagen_Original)
    image2 = Image.open(Imagen_Entrada)

    # Garantizar el formato adecuado para el tratamiento de las imagenes
    if image1.size != image2.size:
        print("Las imagenes no tienen el tamano esperado (20x20 pixeles)")
        exit(1)

    # Inspeccionar cada pixel en busqueda de una discrepancia
    for x in range(image1.width):
        for y in range(image1.height):
            # Obtencion del valor correspondiente al pixel
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            # Comparacion de los pixeles
            if pixel1 != pixel2:
                print("La imagen de entrada no corresponde al valor numerico del numero original.")
                exit(1)

    '''
    Si en la comparativa entre los pixeles de las imagenes no existe diferencia alguna, entonces
    La funcion nunca abortara su ejecucion
    '''
    print("La imagen ingresada corresponde al valor del numero esperado por el programa")

# Implementacion de la funcion operativa
comparar_imagenes(imagen_del_numero_original, imagen_del_numero_entrada)