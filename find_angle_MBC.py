import math


def find_MBC(ab, bc):
    theta = math.atan(ab/bc)
    degrees = round(theta * 180 / math.pi)
    degrees = math.degrees(theta)
    return degrees


#ab = input()
#bc = input()
ab = 10
bc = 10

print(find_MBC(ab, bc))
