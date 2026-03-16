from pygame.math import Vector3 as vec3

class Material:
    color: vec3 = None
    roughness: float = None
    albedo: float = None
    glowing: float = None
    isChessColored: bool = False
    reflectance: vec3 = None
    glowingColor: vec3 = None
    
    def __init__(self, color:vec3=vec3(1), roughness:float=1, albedo:float=0.9, glowing:float=0, isChessColored:bool=False,reflectance:vec3=vec3(1), glowingColor:vec3=vec3(1)):
        self.color = color
        self.roughness = roughness
        self.albedo = albedo
        self.glowing = glowing
        self.isChessColored = isChessColored
        self.reflectance = reflectance
        self.glowingColor = glowingColor