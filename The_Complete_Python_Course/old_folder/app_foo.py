lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        'name': 'Harry',
        'numbers': {1, 2, 3, 4, 5, 6, 7}
    },
    {
        'name': 'Ron',
        'numbers': {2, 8, 10, 12, 13, 9}
    }
]

for player in players:
    matching_numbers = player['numbers'].intersection(lottery_numbers)
    

    print("{} has one {} number correct.".format(player['name'], len(matching_numbers)))
