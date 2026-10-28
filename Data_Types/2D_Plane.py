import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def farthest_point(points):
    return max(points, key=lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2))

points = [(2, 3), (5, 1), (-4, 6), (1, -2)]

print("Points:", points)

p1 = points[0]
p2 = points[1]

print("Distance between", p1, "and", p2, "=", distance(p1, p2))
print("Farthest point from origin:", farthest_point(points))
