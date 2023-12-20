scheme = []

# Read input file and split lines into characters
with open('aoc23/3_gearRatio/input3.txt', 'r') as file:
    for line in file:
        scheme.append(list(line.strip()))

cur_num = []
total_sum = 0

def search2d(matrix, row, col):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    target = ['[', '@', '_', '!', '#', '$','=', '%', '^', '+', '-', '&', '*', '(', ')', '<', '>', '?', '/', '|', '}', '{', '~', ':']

    for x, y in directions:
        new_row, new_col = row + x, col + y
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[new_row]):
            location = matrix[new_row][new_col]
            if location.isdigit() or location.isalpha():
                continue
            if location in target:
                return True
    return False

for row in range(len(scheme)):
    valid = False
    for col in range(len(scheme[row])):
        if scheme[row][col].isdigit():
            cur_num.append(scheme[row][col])
            if search2d(scheme, row, col):
                valid = True
        length = len(scheme[row])
        if ((not scheme[row][col].isdigit()) or (col == len(scheme[row]) - 1) ) and (cur_num):
            num = ''.join(cur_num)
            if valid:
                total_sum += int(num)
                print(total_sum)
            cur_num.clear()
            valid = False
            num = ''

