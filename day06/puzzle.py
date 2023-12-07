"""
input

Time:        60     94     78     82
Distance:   475   2138   1015   1650
"""

def is_win(max_time, push_time, dist):
    return ((max_time - push_time) * push_time) > dist


# test input
#times = (7, 15, 30)
#dist = (9,40, 200)


# real input
times = (60, 94, 78, 82)
dist = (475, 2138, 1015, 1650)


total = 1

for time, dist in zip(times, dist):
    n = 0

    for i in range(time+1):
        if is_win(time, i, dist):
            n+= 1

    total *= n

print("result part 1:", total)



# test input part 2
#time = 71530
#dist = 940200


# real input part 2
time = 60947882
dist = 475213810151650


# go forward from zero speed to start of winning range
dist_traveled = 0
i = 0

while dist_traveled < dist:
    speed = i
    time_left = time - i
    dist_traveled = time_left * speed
    i += 1

start = i-1

# go backward from max speed to end of winning range
dist_traveled = 0
i = time

while dist_traveled < dist:
    speed = i
    time_left = time - i
    dist_traveled = time_left * speed
    i -= 1

end = i+1

print("result part 2", end-start+1)
