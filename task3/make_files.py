import random

for i in range(1,6):
    file_name = 'Cash' + str(i) + '.txt'
    create_file = open(file_name, "w+")
    for period in range(0,17):
        create_file.write("%d \r\n" % (random.uniform(1, 10)))

create_file.close()