# Advanced Python
# AUTHOR: "Armaan Gupta"
# Date: 18th June, 2022

import math

"""
Dunder methods -> Double underscore methods
"""

class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return f"{self.x}i, {self.y}j, {self.z}k"

    def angle(self, unit="radian"):
        { "xy": None, "yz": None, "xz": None }
        if unit == "radian":
            return { "xy": math.atan(self.y/self.x), "yz": math.atan(self.y/self.z), "xz": math.atan(self.x/self.z) }
        elif unit == "degree":
            return { "xy": 180*math.atan(self.y/self.x), "yz": 180*math.atan(self.y/self.z), "xz": 180*math.atan(self.x/self.z) }


v1 = Vector(34, 43)
v2 = Vector(45, 54)
v3 = v1 + v2

print(v3.angle("degree"))

"""

#############################   FILE OPENING   ######################

You can not open a file if it is being used by any other process
for example if a file is opened by any other programming language you can not actually open it from any 
other process, You have to use linux or whatever system you are using to get it's value or write on it
"""

