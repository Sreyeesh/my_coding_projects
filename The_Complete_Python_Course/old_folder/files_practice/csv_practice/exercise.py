import csv
import json


# csv_file = open('csv_file.txt','r')
# json_file = open('exercise_test.json','w')

# team_names = ('TeamName','CountryName','CountryInitials')
# reader = csv.DictReader(csv_file, team_names)

# for row in reader:
#     json.dump(row,json_file)
#     json_file.write('\n')


with open('The_Complete_Python_Course/files_practice/csv_practice/csv_file.txt', 'r') as csv_file:
    reader = csv.DictReader(csv_file, ('Club', 'City', 'Country'))

    with open('The_Complete_Python_Course/files_practice/csv_practice/exercise_test.json', 'w') as json_file:
        json.dump(list(reader), json_file)