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

camera = Camera(vec3(-5,-3,0),vec3(0,0,pi/10))

objects = [
    Plane (vec3(0, 1, 0), vec3(0,-1,0),vec3(0.5,0.5,0.8)),
    Sphere(vec3(5, -0.5, 0),            2,vec3(0.7,0.2,0.2)),
    Sphere(vec3(4,-3,-15),            9,vec3(0.2,0.7,0.2)),
    Sphere(vec3(12, -5, 5),            3,vec3(0.2,0.2,0.7))
]

objects[0].material.roughness=1
objects[1].material.roughness=0
objects[2].material.roughness=0.1
objects[3].material.roughness=1

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