import tkinter as tk
import random

class GridWindow(tk.Tk):
    def __init__(self, width=500, height=500, cell_size=5):
        super().__init__()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.columns = self.width // self.cell_size
        self.rows = self.height // self.cell_size
        self.canvas = tk.Canvas(self, width=self.width, height=self.height)
        self.canvas.pack()
        
        self.green_pixel = [random.randint(0, self.columns-1), random.randint(0, self.rows-1)]
        self.black_pixel = [random.randint(0, self.columns-1), random.randint(0, self.rows-1)]
        
        self.draw_grid()
        self.update_pixels()
        self.move_green_pixel()
        self.after(200, self.move_black_pixel)

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            self.canvas.create_line(x, 0, x, self.height, fill='gray')
        for y in range(0, self.height, self.cell_size):
            self.canvas.create_line(0, y, self.width, y, fill='gray')

    def update_pixels(self):
        # Dibujar píxel verde en su nueva posición
        self.canvas.create_rectangle(self.green_pixel[0]*self.cell_size, self.green_pixel[1]*self.cell_size,
                                     (self.green_pixel[0]+1)*self.cell_size, (self.green_pixel[1]+1)*self.cell_size,
                                     fill='green', tags='pixel')
        # Dibujar píxel negro en su nueva posición
        self.canvas.create_rectangle(self.black_pixel[0]*self.cell_size, self.black_pixel[1]*self.cell_size,
                                     (self.black_pixel[0]+1)*self.cell_size, (self.black_pixel[1]+1)*self.cell_size,
                                     fill='black', tags='pixel')

    def move_green_pixel(self):
        self.green_pixel[0] = (self.green_pixel[0] + random.choice([-1, 1])) % self.columns
        self.green_pixel[1] = (self.green_pixel[1] + random.choice([-1, 1])) % self.rows
        self.update_pixels()
        self.after(200, self.move_green_pixel)

    def move_black_pixel(self):
        if abs(self.black_pixel[0] - self.green_pixel[0]) <= 3 and abs(self.black_pixel[1] - self.green_pixel[1]) <= 3:
            self.after(200, self.move_black_pixel)
            return
        
        if self.black_pixel[0] < self.green_pixel[0]:
            self.black_pixel[0] += 1
        elif self.black_pixel[0] > self.green_pixel[0]:
            self.black_pixel[0] -= 1

        if self.black_pixel[1] < self.green_pixel[1]:
            self.black_pixel[1] += 1
        elif self.black_pixel[1] > self.green_pixel[1]:
            self.black_pixel[1] -= 1

        self.update_pixels()
        self.after(200, self.move_black_pixel)

if __name__ == '__main__':
    app = GridWindow()
    app.mainloop()
