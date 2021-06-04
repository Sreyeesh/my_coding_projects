"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).

"""


"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""


lottery_numbers = {13, 21, 22, 5, 8}


players = [ {'name':'Ross',
            'number':{23,98,5,2,21} 

}, 

{'name': 'Rachel',
 'number': {25,22,8,12,13}

}

]

  
for player in players: 
    print(player['name'],player['number'].intersection(lottery_numbers))
    


print("Hello, {player} {number}.".format(name=player['name'], number=player['number'])





# player_one_match = lottery_numbers.intersection(players[0]["number"])
# print(player_one_match)

# player_two_match = lottery_numbers.intersection(players[1]["number"])
# print(player_two_match)



    
