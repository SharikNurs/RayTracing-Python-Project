from pygame.math import Vector3 as vec3
from random import random
import numpy as np
import math

def getRandomValueNormalDistribution():
    r = random()
    theta = math.pi*2 * r
    rho = math.sqrt(-2 * math.log(r))
    return rho * math.cos(theta)

def getRandomVector():
    return vec3(getRandomValueNormalDistribution(), getRandomValueNormalDistribution(), getRandomValueNormalDistribution()).normalize()

def clamp(minValue:float,value:float,maxValue:float):
    return min(max(value,minValue),maxValue)

def mul(a: vec3, b: vec3):
    return vec3(a.x * b.x, a.y * b.y, a.z * b.z)