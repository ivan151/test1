import random
random_coordinates = open("point.txt", "w+")

for i in range(100):
     random_coordinates.write("%d %s \r\n" % (random.randint(1,100), random.randint(1,100)))

random_coordinates = open("polygon.txt", "w+")

for i in range(4):
     random_coordinates.write("%d %s \r\n" % (random.randint(1,100), random.randint(1,100)))
