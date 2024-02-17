import math
def polyArea(n, a):
    Area=n*pow(a, 2)*0.25*(1/math.tan(math.pi/n))
    return round(Area,2)
print(polyArea(4, 25))