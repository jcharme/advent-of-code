# read input file and create list of input lines
file = open("/home/jcharme/repos/aoc23/4_scratchCards/input4.txt", "r")
input = file.read()
input_list = input.split('\n')


points = 0
for card in input_list:
    winning_nums = [int(i) for i in card.split(':')[1].split('|')[0].split(' ') if i.isdigit()]
    my_nums = [int(i) for i in card.split(':')[1].split('|')[1].split(' ') if i.isdigit()]

    winners = 0
    for num in my_nums:
        if num in winning_nums:
            winners += 1
    points += 2**(winners-1) if winners > 0 else 0
print(points)