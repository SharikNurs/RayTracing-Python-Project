from pygame.math import Vector3 as vec3

class Material:
    color:vec3 = None
    roughness: float = None
    albedo: float = None
    glowing: float = None
    
    def __init__(self, color:vec3=vec3(1), roughness:float=1, albedo:float=0.8, glowing:float=0):
        self.color = color
        self.roughness = roughness
        self.albedo = albedo
        self.glowing = glowing