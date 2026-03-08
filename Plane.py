from pygame.math import Vector3 as vec3
from intersection import planeIntersection
from IObject import IObject

class Plane(IObject):
    def __init__(self,pos:vec3,normal:vec3,color:vec3):
        self.pos = pos
        self.normal = normal
        self.color = color
        self.roughness = 1
        self.brightness = 0
        
    def setMaterial(self,roughness:float=1, brightness:float=0):
        self.roughness = roughness
        self.brightness = brightness
    
    def intersection(self,origin:vec3,direction:vec3):
        return planeIntersection(origin,direction,self.pos,self.normal)

    def getNormal(self,v:vec3):
        return self.normal