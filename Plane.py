from pygame.math import Vector3 as vec3
from pygame.math import Vector2 as vec2
from intersection import planeIntersection
from IObject import IObject

class Plane(IObject):
    def __init__(self,pos:vec3,normal:vec3,color:vec3):
        self.pos = pos
        self.normal = normal
        self.color = color
        self.roughness = 0.1
        
    def setMaterial(self,roughness:float):
        self.roughness = roughness
    
    def intersection(self,origin:vec3,direction:vec3):
        return planeIntersection(origin,direction,self.pos,self.normal)

    def getNormal(self,v:vec3):
        return self.normal