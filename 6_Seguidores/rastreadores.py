import tkinter as tk
import random

def draw_grid(canvas, width, height, cell_size):
    for x in range(0, width, cell_size):
        canvas.create_line(x, 0, x, height, fill='gray')
    for y in range(0, height, cell_size):
        canvas.create_line(0, y, width, y, fill='gray')

def update_pixels(canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo):
    canvas.delete('pixel')
    canvas.create_rectangle(pixel_corredor_azul[0]*cell_size, pixel_corredor_azul[1]*cell_size,
                            (pixel_corredor_azul[0]+1)*cell_size, (pixel_corredor_azul[1]+1)*cell_size,
                            fill='blue', tags='pixel')
    canvas.create_rectangle(pixel_seguidor_rojo[0]*cell_size, pixel_seguidor_rojo[1]*cell_size,
                            (pixel_seguidor_rojo[0]+1)*cell_size, (pixel_seguidor_rojo[1]+1)*cell_size,
                            fill='red', tags='pixel')

def move_green_pixel(canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo, columns, rows):
    pixel_corredor_azul[0] = (pixel_corredor_azul[0] + random.choice([-1, 1])) % columns
    pixel_corredor_azul[1] = (pixel_corredor_azul[1] + random.choice([-1, 1])) % rows
    update_pixels(canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo)
    root.after(200, move_green_pixel, canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo, columns, rows)

def move_black_pixel(canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo, columns, rows):
    if abs(pixel_seguidor_rojo[0] - pixel_corredor_azul[0]) <= 3 and abs(pixel_seguidor_rojo[1] - pixel_corredor_azul[1]) <= 3:
        root.after(200, move_black_pixel, canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo, columns, rows)
        return

    if pixel_seguidor_rojo[0] < pixel_corredor_azul[0]:
        pixel_seguidor_rojo[0] += 1
    elif pixel_seguidor_rojo[0] > pixel_corredor_azul[0]:
        pixel_seguidor_rojo[0] -= 1

    if pixel_seguidor_rojo[1] < pixel_corredor_azul[1]:
        pixel_seguidor_rojo[1] += 1
    elif pixel_seguidor_rojo[1] > pixel_corredor_azul[1]:
        pixel_seguidor_rojo[1] -= 1

    update_pixels(canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo)
    root.after(200, move_black_pixel, canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo, columns, rows)

if __name__ == '__main__':
    width = 500
    height = 500
    cell_size = 5
    columns = width // cell_size
    rows = height // cell_size

    pixel_corredor_azul = [random.randint(0, columns-1), random.randint(0, rows-1)]
    pixel_seguidor_rojo = [random.randint(0, columns-1), random.randint(0, rows-1)]

    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    draw_grid(canvas, width, height, cell_size)
    update_pixels(canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo)
    move_green_pixel(canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo, columns, rows)
    root.after(200, move_black_pixel, canvas, cell_size, pixel_corredor_azul, pixel_seguidor_rojo, columns, rows)

    root.mainloop()
