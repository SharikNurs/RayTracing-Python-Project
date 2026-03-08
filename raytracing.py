from functions import getRandomVector
from pygame.math import Vector3 as vec3
from random import random
from data import setting




def rayTracing(origin,direction,figures,entryColor:vec3=vec3(0),bounces:int=0,reflectionsNum=1.0):
    ray = emitRay(origin,direction,figures)
    
    color = entryColor.copy()

    if not ray[2]:
        color += vec3(*setting['bg_color']) / reflectionsNum
        return color
    
    color += ray[1].color / reflectionsNum
    
    if ray[1].roughness < 1 and bounces > 0:
        pos = origin + direction*ray[0]
        normal = ray[1].getNormal(pos)
        pos += normal * 0.001
        reflected = direction.reflect(normal)
        if ray[1].roughness > 0:
            reflected += ray[1].roughness * getRandomVector()
            reflected = reflected.normalize()

        color = rayTracing(pos,reflected,figures,color,bounces-1,reflectionsNum+1)
    
    return color



def emitRay(origin,direction,figures):
    t = -1
    obj = None
    collision = False

    for figure in figures:
        r = figure.intersection(origin,direction)
        if r < 0:
            continue

        if t < 0 or r < t:
            t = r
            obj = figure
            collision = True
    
    return [t, obj, collision]