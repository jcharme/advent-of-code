time = [41,77,70,96]
record = [249,1362,1127,1011]

race= [0, 0, 0, 0]

for i in range(4):
    for j in range(time[i]):
        distance = j * (time[i] - j)
        if distance > record[i]:
                race[i] += 1

print(race)
count = 1
for i in race:
    count *= i

print(count)