from functions import getRandomVector, mul
from pygame.math import Vector3 as vec3
from random import random
from data import setting




def rayTracing(origin,direction,figures,entryColor:vec3=vec3(1),bounces:int=0,reflectionsNum:int=0,entryLight:vec3=vec3(0),absorbedlight:float=1):
    ray = emitRay(origin,direction,figures)
    
    color = entryColor.copy()
    incomingLight = entryLight.copy()
    n = absorbedlight

    if not ray[2]:
        sky_color = vec3(setting['sky_color']) / 255 * n
        color = mul(color,sky_color)
        incomingLight += color * setting['sky_glowing']
        return (color, incomingLight, n)
    
    n *= ray[1].material.albedo

    color = mul(color,ray[1].material.color * n)
    
    # chess like plane
    if ray[1].material.isChessColored:
        pos = origin + direction*ray[0]
        if (pos.x // 1.5 + pos.z // 1.5) % 2 == 0:
            color = mul(color,ray[1].material.color * n)
        else:
            color = mul(color,ray[1].material.color / 2 * n)

    incomingLight += (ray[1].material.glowing * color)
    
    if bounces > 0:
        # reflect the light
        pos = origin + direction*ray[0]
        normal = ray[1].getNormal(pos)
        pos += normal * 0.001
        reflected = direction.reflect(normal)

        # roughness(randomness) to the light
        randomVector = getRandomVector()
        if randomVector.dot(normal) < 0:
            randomVector = - randomVector

        reflected = (1 - ray[1].material.roughness) * reflected + ray[1].material.roughness * randomVector
        reflected = reflected.normalize()

        color, incomingLight, n = rayTracing(pos,reflected,figures,color,bounces-1,reflectionsNum+1,entryLight=incomingLight,absorbedlight=n)
    
    return (color, incomingLight, n)



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