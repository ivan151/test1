import sys
from sympy import *

point_input = str(sys.argv[1])
polygon_input = str(sys.argv[2])

with open(point_input, 'r') as point_coord:
    point_coord_list = []
    point_coordinates = point_coord.readlines()
    for i in range(0, len(point_coordinates)):
        pointpc = tuple(map(int, point_coordinates[i].split()))
        point_coord_list.append(pointpc)

with open(polygon_input, 'r') as polyg_coord:
    polygon_coordinates_list = []
    polygon_coordinates = polyg_coord.readlines()
    for i in range(0, len(polygon_coordinates)):
        pc = tuple(map(int, polygon_coordinates[i].split()))
        polygon_coordinates_list.append(pc)

p1 = polygon_coordinates_list[0]
p2 = polygon_coordinates_list[1]
p3= polygon_coordinates_list[2]
p4 = polygon_coordinates_list[3]

polygon = Polygon(p1, p2, p3, p4)

sides = polygon.sides
t = Point2D(0,4)
s = Segment2D(Point2D(2,4), Point2D(0,4))
vertices = polygon.vertices

for coord in point_coord_list:
    x,y = coord[0],coord[1]
    point = Point2D(x,y)
    if point in vertices:
        print(0)
    else:
        for side in sides:
            if point in side:
                print(1)
    if polygon.encloses_point(point):
        print(2)
    else:
        print(3)
