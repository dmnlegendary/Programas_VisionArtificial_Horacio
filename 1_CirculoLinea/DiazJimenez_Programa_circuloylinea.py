'''
Programa no.1 "Trazado de Línea y Círculo"

Materia: Visión Artificial

Grupo: 5BV1

Alumno: Díaz Jiménez Jorge Arif
'''

import pygame
import sys

# Ajuste de tamanos de ancho y largo
ancho, altura = 600, 400
# Caracteristicas del circulo
centroEnX, centroEnY = ancho // 2, altura // 2
radio = 100
# Caracteristicas de la linea
Inicio_linea = (250, 100)
Fin_linea = (500, 350)

# Cargar pygame para manipular pixeles
pygame.init()
# Crear la ventana del trabajo
ventana = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Circulo y linea")

# Algoritmno de medio punto para el circulo
def dibujar_circulo(xc, yc, radio):
    x = radio
    y = 0
    decision = 1 - radio
    points = []
    while y <= x:
        points.append((xc + x, yc + y))
        points.append((xc - x, yc + y))
        points.append((xc + x, yc - y))
        points.append((xc - x, yc - y))
        points.append((xc + y, yc + x))
        points.append((xc - y, yc + x))
        points.append((xc + y, yc - x))
        points.append((xc - y, yc - x))
        y += 1
        if decision <= 0:
            decision += 2 * y + 1
        else:
            x -= 1
            decision += 2 * (y - x) + 1
    return points

# Algoritmo Bresenham
def dibujar_linea(start, end):
    x1, y1 = start
    x2, y2 = end
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    points = []
    while x1 != x2 or y1 != y2:
        points.append((x1, y1))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy
    points.append((x2, y2))
    return points

# Dibujar el circulo
puntos_del_circulo = dibujar_circulo(centroEnX, centroEnY, radio)
for point in puntos_del_circulo:
    ventana.set_at(point, (255, 120, 120))

# Dibujar la linea
line_points = dibujar_linea(Inicio_linea, Fin_linea)
for point in line_points:
    ventana.set_at(point, (0, 0, 255))

# Ciclo principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# abortar Pygame
pygame.quit()
sys.exit()