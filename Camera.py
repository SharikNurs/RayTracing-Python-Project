from pygame.math import Vector3 as vec3
from pygame.math import Vector2 as vec2
from data import setting
from math import sin, cos

class Camera:
    def __init__(self, pos:vec3, facing:vec3):
        self.pos = pos
        self.facing = facing
    
    def rotateX(self,v,angle):
        c = cos(angle)
        s = sin(angle)
        return vec3(
            v.x,
            v.y*c + v.z*(-s),
            v.y*s + v.z*c
        )

    def rotateY(self,v,angle):
        c = cos(angle)
        s = sin(angle)
        return vec3(
            v.x*c + v.z*s,
            v.y,
            v.x*(-s) + v.z*c
        )
    
    def rotateZ(self,v,angle):
        c = cos(angle)
        s = sin(angle)
        return vec3(
            v.x*c + v.y*(-s),
            v.x*s + v.y*c,
            v.z
        )
    
    def getRayDirection(self,y,x):
        ratio = setting['height']/setting['width']
        uv = vec2(y/setting['height'],x/setting['width'])
        uv = uv * 2 - vec2(1)
        uv.x *= ratio

        direction = vec3(1,uv.x,uv.y)

        direction = self.rotateX(direction,self.facing.x)
        direction = self.rotateY(direction,self.facing.y)
        direction = self.rotateZ(direction,self.facing.z)

        return direction