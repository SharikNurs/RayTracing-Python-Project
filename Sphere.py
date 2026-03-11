from pygame.math import Vector3 as vec3
from intersection import sphereIntersection
from Material import Material
from IObject import IObject

class Sphere(IObject):
    def __init__(self,pos:vec3,radius:float,color:vec3):
        self.pos = pos
        self.radius = radius
        self.material = Material(color)
    
    def intersection(self,origin:vec3,direction:vec3):
        return sphereIntersection(origin,direction,self.pos,self.radius)

    def getNormal(self,v:vec3):
        return (v-self.pos).normalize()