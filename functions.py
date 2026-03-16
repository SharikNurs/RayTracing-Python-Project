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

def SchlicksApproximation(rayDir:vec3,normal:vec3,reflectance:vec3,incomingLight:vec3):
    # 1. Calculate the cosine of the angle
    cos_theta = clamp(0,normal.dot(-rayDir),1)

    # 2. Apply Schlick's Approximation
    R0 = reflectance # Gold
    F = R0 + (vec3(1.0) - R0) * pow(1.0 - cos_theta, 5)

    # 3. Use F to tint the reflected ray
    return mul(F, incomingLight)