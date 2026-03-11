from pygame.math import Vector3 as vec3
from abc import ABC, abstractmethod


class IObject(ABC):
    @abstractmethod
    def intersection(self,origin:vec3,direction:vec3):
        ...

    @abstractmethod
    def getNormal(self,v:vec3):
        ...