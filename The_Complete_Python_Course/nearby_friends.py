"""
Project: near_by_friends

Author : Sreyeesh Garimella 

Date: 4/22/2021


"""

nearby_people = {'Rolf','Jen', 'Anna'}
user_friends = set()


#Ask the user for the name of a friend 

friend_name = input('What is your friends name ? ')

# Add the name to the empty set

user_friends.add(friend_name)

    
 # Print out the intersection between both sets. This gives us a set with those friends that are nearby.
print("nearby_people intersection of user_friends: ",user_friends.intersection(nearby_people))
   