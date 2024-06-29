import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageTk
import cv2
import numpy as np

class ColorSegmentationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Segmentacion de colores por RGB")
        
        self.img_label = tk.Label(root)
        self.img_label.pack()
        
        self.load_button = tk.Button(root, text="Cargar imagen", command=self.load_image)
        self.load_button.pack()
        
        self.color1_button = tk.Button(root, text="Escoger limite inferior RGB", command=self.choose_lower_color)
        self.color1_button.pack()
        
        self.color2_button = tk.Button(root, text="Escoger limite superior RGB", command=self.choose_upper_color)
        self.color2_button.pack()
        
        self.segment_button = tk.Button(root, text="Segmentar imagen", command=self.segment_image)
        self.segment_button.pack()
        
        self.lower_color = (0, 0, 0)
        self.upper_color = (255, 255, 255)
        self.image = None
        self.cv_image = None
        
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image = self.resize_image(self.image)
            self.cv_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_RGB2BGR)
            self.display_image(self.image)
        
    def choose_lower_color(self):
        color_code = colorchooser.askcolor(title="Seleccion del limite inferior")[0]
        if color_code:
            self.lower_color = tuple(map(int, color_code))
            print(f"Seleccione limite de RGB inferior: {self.lower_color}")
        
    def choose_upper_color(self):
        color_code = colorchooser.askcolor(title="Seleccion del limite superior")[0]
        if color_code:
            self.upper_color = tuple(map(int, color_code))
            print(f"Seleccione limite de RGB superior: {self.upper_color}")
        
    def segment_image(self):
        if self.cv_image is not None:
            lower_bound = np.array([self.lower_color[2], self.lower_color[1], self.lower_color[0]]) 
            upper_bound = np.array([self.upper_color[2], self.upper_color[1], self.upper_color[0]]) 
            
            mask = cv2.inRange(self.cv_image, lower_bound, upper_bound)
            result = cv2.bitwise_and(self.cv_image, self.cv_image, mask=mask)
            result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
            
            segmented_image = Image.fromarray(result)
            self.display_image(segmented_image)
            
    def resize_image(self, img):
        max_size = 500
        img.thumbnail((max_size, max_size))
        return img
        
    def display_image(self, img):
        imgtk = ImageTk.PhotoImage(image=img)
        self.img_label.config(image=imgtk)
        self.img_label.image = imgtk

if __name__ == "__main__":
    root = tk.Tk()
    app = ColorSegmentationApp(root)
    root.mainloop()
