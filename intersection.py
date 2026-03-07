from pygame.math import Vector3 as vec3
from math import *

def sphereIntersection(origin:vec3,direction:vec3,sPos:vec3,r:float):
    O = origin - sPos
    a = direction.x**2 + direction.y**2 + direction.z**2
    b = 2*O.x*direction.x + 2*O.y*direction.y + 2*O.z*direction.z
    c = O.x**2 + O.y**2 + O.z**2 - r**2

    D = b**2 - 4*a*c

    if D < 0:
        return -1
    
    if D == 0:
        t = -b / (2 * a)
        return t
    
    s1 = (-b + sqrt(D)) / (2 * a)
    s2 = (-b - sqrt(D)) / (2 * a)
    return min(s1,s2)

def planeIntersection(origin:vec3,direction:vec3,plane:vec3,normal:vec3):
    dot = direction.dot(normal)

    if abs(dot) < 0.0001:
        return -1

    t = plane - origin
    t *= normal
    t /= direction.dot(normal)
    
    if t < 0:
        return -1
    
    return t