file = open("/home/jcharme/repos/aoc23/4_scratchCards/input4.txt", "r")
input = file.read()
input_list = input.split('\n')

cards = [1]*len(input_list)
for ind_card, card in enumerate(input_list):
    winning_nums = [int(i) for i in card.split(':')[1].split('|')[0].split(' ') if i.isdigit()]
    my_nums = [int(i) for i in card.split(':')[1].split('|')[1].split(' ') if i.isdigit()]
    
    winners = 0
    for num in my_nums:
        if num in winning_nums:
            winners += 1

    for i in range(0,winners):
        if ind_card+i+1 < len(input_list):
            cards[ind_card+i+1] += cards[ind_card]

print(sum(cards))