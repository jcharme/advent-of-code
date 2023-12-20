time = 41777096
record = 249136211271011

race = 0


for j in range(time):
    distance = j * (time - j)
    if distance > record:
            race += 1

print(race)