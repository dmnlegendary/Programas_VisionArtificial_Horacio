import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
negro = (0, 0, 0)
blanco = (255, 255, 255)
rojo = (255, 0, 0)
verde = (0, 255, 0)

# Dimensiones de la pantalla
ancho = 400
alto = 400

# Crear la pantalla
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Dos pixeles con rastro")

# Lista para almacenar los colores del rastro
rastro_rojo = []
rastro_verde = []

# Posición inicial del pixel aleatorio
x_aleatorio = random.randint(0, ancho - 1)
y_aleatorio = random.randint(0, alto - 1)

# Posición inicial del pixel seguidor
x_seguidor = x_aleatorio
y_seguidor = y_aleatorio

# Velocidad de los pixeles
velocidad_aleatoria = 1
velocidad_seguidora = 2

# Bucle principal del juego
fin = False
while not fin:
    # Revisar eventos del teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True

    # Mover el pixel aleatorio de forma aleatoria
    x_aleatorio += random.choice([-velocidad_aleatoria, 0, velocidad_aleatoria])
    y_aleatorio += random.choice([-velocidad_aleatoria, 0, velocidad_aleatoria])

    # Limitar el pixel aleatorio a la cuadrícula
    x_aleatorio = max(0, min(x_aleatorio, ancho - 1))
    y_aleatorio = max(0, min(y_aleatorio, alto - 1))

    # Mover el pixel seguidor hacia el pixel aleatorio
    x_seguidor += (x_aleatorio - x_seguidor) // velocidad_seguidora
    y_seguidor += (y_aleatorio - y_seguidor) // velocidad_seguidora

    # Agregar los colores actuales al rastro
    rastro_rojo.append((x_aleatorio, y_aleatorio, rojo))
    rastro_verde.append((x_seguidor, y_seguidor, verde))

    # Eliminar los colores antiguos del rastro
    if len(rastro_rojo) > 100:
        rastro_rojo.pop(0)
    if len(rastro_verde) > 100:
        rastro_verde.pop(0)

    # Rellenar la pantalla de negro
    pantalla.fill(negro)

    # Dibujar el rastro
    for (x, y, color) in rastro_rojo:
        pygame.draw.rect(pantalla, color, (x, y, 1, 1))
    for (x, y, color) in rastro_verde:
        pygame.draw.rect(pantalla, color, (x, y, 1, 1))

    # Dibujar los pixeles
    pygame.draw.rect(pantalla, rojo, (x_aleatorio, y_aleatorio, 1, 1))
    pygame.draw.rect(pantalla, verde, (x_seguidor, y_seguidor, 1, 1))

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
