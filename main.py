from pygame.math import Vector3 as vec3

import numpy as np
from math import pi
from time import time

from Sphere import Sphere
from Plane import Plane

from raytracing import emitRay, rayTracing
from Camera import Camera

from functions import clamp
from data import setting
from save import Save


image = np.zeros((setting['height'],setting['width'],3),np.uint8)

camera = Camera(vec3(-3,0,0),vec3(0,0,0))

objects = [
    Plane(vec3(0,4,0),vec3(0,-1,0),vec3(1)),
    Plane(vec3(0,-4,0),vec3(0,1,0),vec3(1)),
    Plane(vec3(0,0,4),vec3(0,0,-1),vec3(0.2,1,0.2)),
    Plane(vec3(0,0,-4),vec3(0,0,-1),vec3(1,0.2,0.2)),
    Plane(vec3(8,0,0),vec3(-1,0,0),vec3(1,1,1)),
    Plane(vec3(-4,0,0),vec3(1,0,0),vec3(0)),

    Sphere(vec3(4,0,0), 2.5, vec3(1)),
]

objects[0].material.isChessColored = True
objects[1].material.glowing = 1.5

startTime = time()

for y in range(setting['height']):
    for x in range(setting['width']):
        direction = camera.getRayDirection(y,x)

        result = vec3(0)
        for iter in range(1, setting['triesPerPixel']+1):
            color = rayTracing(origin=camera.pos,direction=direction,figures=objects,bounces=setting['reflections'])[1]
            result += color / setting['triesPerPixel']

        image[y][x][0] = clamp(0,int(result.x*255),255)
        image[y][x][1] = clamp(0,int(result.y*255),255)
        image[y][x][2] = clamp(0,int(result.z*255),255)

print(f"\n\nCalculations took {time()-startTime:.2f} seconds\n\n")

Save(image)