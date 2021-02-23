"""
Name: Sreyeesh Garimella

Project: Nearby Friends

Date:  18/12/2019


"""

nearby_people = {'Rolf', 'Jen', 'Anna'}

user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
user_friend = input("Please enter your friends name:")
print("Thank you for entering the name:",user_friend)

# Add the name to the empty set
user_friends.add(user_friend)
print(user_friends) 

# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
user_friend = nearby_people.intersection(user_friends)
print(user_friend)