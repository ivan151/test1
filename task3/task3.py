import sys
from sympy import *

dir = str(sys.argv[1])

max_periods = []
for i in range(1,6):
    with open(f'{dir}/Cash{i}.txt', 'r') as cash_file:
        each_cash_values = cash_file.readlines()
        for i in range(0,len(each_cash_values)):
            each_cash_values[i] = int(each_cash_values[i])
        max_period_of_each_cash = each_cash_values.index(max(each_cash_values))
        max_periods.append(max_period_of_each_cash)

max_period = max(set(max_periods), key = max_periods.count)

print(max_period)


