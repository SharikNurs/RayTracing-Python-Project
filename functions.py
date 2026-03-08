from pygame.math import Vector3 as vec3
from random import random
import numpy as np

def getRandomVector():
    return vec3(random()*2-1, random()*2-1, random()*2-1)

def clamp(minValue:float,value:float,maxValue:float):
    return min(max(value,minValue),maxValue)