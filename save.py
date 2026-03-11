from PIL import Image
import numpy as np

def Save(image,floats:bool=False):
    if floats:
        for y in range(len(image)):
            for x in range(len(image[0])):
                for c in range(len(image[0][0])):
                    image[y][x][c] = np.uint8(255 * image[y][x][c])
                    
    img = Image.fromarray(image)
    img.save("result.png")