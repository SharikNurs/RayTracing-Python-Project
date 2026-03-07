from PIL import Image
import numpy as np

def Save(image,floats:bool=False):
    if floats:
        for y in image:
            for x in y:
                for c in x:
                    c: np.uint8 = int(c*255)
                    
    img = Image.fromarray(image)
    img.save("result.png")