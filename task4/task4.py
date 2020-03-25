from sympy import Point, Line

p1, p2 = Point(1000, 0), Point(10, 20)
l1 = Line(p1, p2)
print(l1.length)

time = '8:30 9:30'
time1 = '8:00 8:30'
time2 = '8:15 8:45'
time3 = '8:45 9:00'
time4 = '8:30 9:00'
time5 = '9:00 9:30'
time6 = '9:10 9:20'


def convert_to_min(time_string):
    t = time.split()
    l = []
    l1 =[]
    for s in t:
        t1 = s.split(':')
        l.append(t1)
    enter_in_minutes = int(l[0][0]) * 60 + int(l[0][1])
    exit_in_minutes = int(l[1][0]) * 60 + int(l[1][1])
    for minute in range(enter_in_minutes, exit_in_minutes):
        l1.append(minute)
    return(l1)

all_times = [time1,time2,time3,time4,time5,time6]


