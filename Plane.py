from pygame.math import Vector3 as vec3
from intersection import planeIntersection
from Material import Material
from IObject import IObject

class Plane(IObject):
    def __init__(self,pos:vec3,normal:vec3,color:vec3):
        self.pos = pos
        self.normal = normal
        self.material = Material(color)
    
    def intersection(self,origin:vec3,direction:vec3):
        return planeIntersection(origin,direction,self.pos,self.normal)

    def getNormal(self,v:vec3):
        return self.normal