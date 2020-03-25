import random
random_numbers = open("random_numbers.txt", "w+")

for i in range(1000):
     random_numbers.write("%d\r\n" % random.randint(-32768,32768))

random_numbers.close()