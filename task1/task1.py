import sys
import numpy as np

input_filename = str(sys.argv[1])

with open(input_filename, 'r') as input_file:
    array_of_numbers = input_file.readlines()
    for i in range(0,len(array_of_numbers)):
        array_of_numbers[i] = int(array_of_numbers[i])
    percentile = np.percentile(array_of_numbers,90)
    mediana = np.median(array_of_numbers, axis=0)
    average = np.average(array_of_numbers)
    max_number = max(array_of_numbers)
    min_number = min(array_of_numbers)
    print(percentile)
    print(mediana)
    print(max_number)
    print(min_number)
    print(average)
