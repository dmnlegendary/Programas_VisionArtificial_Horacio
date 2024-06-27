from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def load_image(image_path):
    img = Image.open(image_path).convert('RGB')
    return np.array(img)

def animate_transition(img1, img2, steps=30, interval=100):
    fig, ax = plt.subplots()
    img_display = ax.imshow(img1)
    ax.axis('off')

    # Get the coordinates of the pixels to transition
    # We are using only the red channel for comparison
    start_y, start_x = np.where(img1[:, :, 0] != img2[:, :, 0])
    
    if len(start_y) != 1 or len(start_x) != 1:
        raise ValueError("There should be exactly one differing pixel in each image")

    end_y, end_x = start_y[0], start_x[0]

    # Initialize positions
    current_y, current_x = start_y[0], start_x[0]

    def update_frame(step):
        nonlocal current_y, current_x
        
        # Calculate the next position
        dy = (end_y - current_y) / steps
        dx = (end_x - current_x) / steps
        
        if step > 0:
            # Move the current pixel towards the target pixel
            img1[current_y, current_x] = img2[end_y, end_x]
            current_y += dy
            current_x += dx
            current_y = int(round(current_y))
            current_x = int(round(current_x))
            img1[current_y, current_x] = img2[end_y, end_x]

        img_display.set_array(img1)
        return [img_display]

    ani = animation.FuncAnimation(fig, update_frame, frames=range(steps + 1), interval=interval, blit=True)
    plt.show()

# Load images
image1_path = 'charger_2008.png'
image2_path = 'Federal_police_F150_2.png'

img1 = load_image(image1_path)
img2 = load_image(image2_path)

# Ensure images have the same shape
if img1.shape != img2.shape:
    raise ValueError("Images must have the same dimensions")

# Animate transition
animate_transition(img1, img2)
