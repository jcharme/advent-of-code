import fileinput

scheme = []
for line in fileinput.input(files =('/home/jcharme/repos/aoc23/3_gearRatio/input3.txt')): #Make each line an element of an array to create 2d array
    scheme.append(list(line))

print(scheme)

for row in range(len(scheme)):
    for col in range(len(scheme[0])):
        current = scheme[]


#Check each direction in 2d array for a symbol
# for x, y in [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]: # directions
