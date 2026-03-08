class vec3:
    def __init__(self,x:float=0,y:float=0,z:float=0):
        self.x:float = x
        self.y:float = y
        self.z:float = z
    
    def __add__(self, other):
        if type(other) == vec3:
            print("yes")

a = vec3()
b = vec3()
a + b