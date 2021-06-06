

lottery_numbers = {13, 21, 22, 5, 8}


players = [{'name': 'Ross',
            'numbers': {23, 98, 5, 2, 21}

            },

           {'name': 'Rachel',
            'numbers': {25, 22, 8, 12, 13}

            }

           ]


for player in players:
    numbers_correct = player['numbers'].intersection(lottery_numbers)
    print('Player {} got {} numbers right.'.format(player['name'],len(numbers_correct)))