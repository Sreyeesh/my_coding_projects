

lottery_numbers = {13, 21, 22, 5, 8}


players = [{'name': 'Ross',
            'numbers': {23, 98, 5, 2, 21}

            },

           {'name': 'Rachel',
            'numbers': {25, 22, 8, 12, 13}

            }

           ]


<<<<<<< HEAD
for player in players: 
    player_one_name = players[0]['name']
    player_two_name = players[1]['name']
    numbers_correct = player['number'].intersection(lottery_numbers)
    print(f" {player_one_name} got {len(numbers_correct)} numbers right.")
    print(f" {player_two_name} got {len(numbers_correct)} numbers right.")
    print('Hello,{}.You matched these numbers {} right'.format(player['name'],numbers_correct))
  
=======
for player in players:
    numbers_correct = player['numbers'].intersection(lottery_numbers)
    print('Player {} got {} numbers right.'.format(player['name'],len(numbers_correct)))
>>>>>>> fd10d15f1905bcc2e2a7a669e3d99b2a37cc8585
