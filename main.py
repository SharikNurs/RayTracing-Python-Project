from pygame.math import Vector3 as vec3
from pygame.math import Vector2 as vec2

import numpy as np
from math import pi
from random import random

from Sphere import Sphere
from Plane import Plane
from raytracing import emitRay
from Camera import Camera

from data import setting
from save import Save


def reflect(direction:vec3, normal:vec3):
    return direction - 2 * direction.dot(normal) * normal

def getRandomVector():
    return vec3(random()*2-1,random()*2-1,random()*2-1).normalize()


image = np.zeros((setting['height'],setting['width'],3),np.uint8)

camera = Camera(vec3(-3,0,0),vec3())

objects = [
    Plane (vec3(8,6, 0),vec3(0,-1,0),vec3(0.5,0.5,0.8)),
    Sphere(vec3(8,0, 0),           2,vec3(0.7,0.2,0.2)),
    Sphere(vec3(8,-4,0),           1,vec3(0.2,0.7,0.2)),
    Sphere(vec3(8,0, 3),           1,vec3(0.2,0.2,0.7))
]

lightSources = [Sphere(vec3(5,-3,-4),1,vec3(1))]

for y in range(setting['height']):
    for x in range(setting['width']):
        accumulateColor = [0,0,0]

        for n in range(setting['triesPerPixel']):
            direction = camera.getRayDirection(y,x)

            first = emitRay(camera.pos,direction,objects)

            if not first[2]: # end if there weren't any collisions
                continue

            # pos = camera.pos + direction*first[0]
            # normal = (pos-first[1].pos).normalize()
            # normal += vec3(1)
            # normal /= 2
            # normal *= 255
            # image[y][x] = [normal.x,normal.y,normal.z]

            pos = camera.pos + direction*first[0]
            normal = first[1].getNormal(pos)
            pos += normal * 0.001
            lightDirection = (lightSources[0].pos-pos).normalize()
            # reflected = reflect(direction,normal)
            second = emitRay(pos,lightDirection,objects)

            if second[2] and second[0] <= (lightSources[0].pos-pos).length(): # end if there was a collision between a ray and some object on it's way to the light source
                continue

            c = max(0,normal.dot(lightDirection))*255
            accumulateColor[0] += first[1].color.x * c / setting['triesPerPixel']
            accumulateColor[1] += first[1].color.y * c / setting['triesPerPixel']
            accumulateColor[2] += first[1].color.z * c / setting['triesPerPixel']
        
        image[y][x] = accumulateColor


Save(image)