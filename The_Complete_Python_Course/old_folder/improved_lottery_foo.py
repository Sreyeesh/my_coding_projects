"""
Project: Improved Lotter system

Author: Sreyeesh 

Date: 13/1/2020


"""

import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# Here are your players; find out who has the most numbers matching lottery_numbers!
players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# matched_numbers = {}

top_player = None
top_score = 0

for player in players:
    matched_numbers = player["numbers"].intersection(lottery_numbers)
    score = 100 ** len(matched_numbers)

    if score > top_score:
        top_score = score  
        top_player = player["name"]


print("{} won ${}.00".format(top_player,top_score))






