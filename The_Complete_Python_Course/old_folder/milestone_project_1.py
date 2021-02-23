"""
Project: Movie Database
Author: Sreyeesh 
20/01/2020
"""
movies = []
 
def menu():
    # ask user for input
    user_input = input("\nPlease enter '1' to add a new movie, '2' to show movies, '3' to find a movie and 'q' to quit running the application: ")
    

    while user_input != 'q':
        if user_input == '1':
            add_movies()
        elif user_input == '2':
            show_movies()
        elif user_input == '3':
            find_movie()
        else:
            print('Unknown command, please enter a valid command!') 
        user_input = input("\nPlease enter '1' to add a new movie,'2' to show movies, '3' to find a movie and 'q' to quit running the application: ")
    print('Exiting the app')
 
        
        
def add_movies():
    title = input("Enter movie title: ")
    director = input("Enter movie director: ")
    year = input("Enter movie realease year: ")
    
    movie = {
        'title': title.strip(),
        'director': director.strip(),
        'year': year
    }
    
    movies.append(movie)
    
     
def show_movies():
    for movie in movies:
        print(movie)
 
def find_movie():
    user_input = input('Please enter movie details:')
    found = False
    for movie in movies:
        if user_input in movie.values():
            print(movie)
            found = True

    if not found:
        print('{} not in database'.format(user_input))
            
menu()







