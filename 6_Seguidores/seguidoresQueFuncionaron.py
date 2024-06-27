import cv2
import numpy as np
import random

def move_towards(src, dest, step=1):
    """
    Move src pixel towards dest pixel by a step.
    """
    direction = np.array(dest) - np.array(src)
    distance = np.linalg.norm(direction)
    
    if distance < step:
        return dest
    else:
        direction = direction / distance
        return np.array(src) + direction * step

def transition_pixel_by_pixel(img1, img2, steps=50000, step_size=1):
    """
    Transition between two images by moving pixels from img1 to img2.
    """
    assert img1.shape == img2.shape, "Images must be of the same size."
    
    rows, cols, _ = img1.shape
    current_img = img1.copy()
    
    # Initialize two random pixels
    px1 = [random.randint(0, rows-1), random.randint(0, cols-1)]
    px2 = [random.randint(0, rows-1), random.randint(0, cols-1)]
    
    for _ in range(steps):
        # Move px2 towards px1
        px2 = move_towards(px2, px1, step=step_size)
        
        # Ensure pixel coordinates are integers
        px2 = [int(round(px2[0])), int(round(px2[1]))]
        
        # Copy pixel value from img2 to current_img
        current_img[tuple(px2)] = img2[tuple(px2)]
        
        # Randomly move px1
        px1[0] = (px1[0] + random.choice([-5, 0, 5])) % rows
        px1[1] = (px1[1] + random.choice([-5, 0, 5])) % cols
        
        cv2.imshow("Pixel by Pixel Transition", current_img)
        cv2.waitKey(1)
    
    cv2.imshow("Pixel by Pixel Transition", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Load images
img1 = cv2.imread('Armored_Federal_Van.jpg')
img2 = cv2.imread('Federal_police_ram1500.jpg')

# Resize images to 500x500
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

# Perform the pixel by pixel transition
transition_pixel_by_pixel(img1, img2)
