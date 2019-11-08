"""
Tasks

[x] Main interface
[x] Add movies
[x] List movies
[] Edit movies
[x] Remove movies
[] Search movies
[x] Exit program
"""

print("""
    #############################################################################################################
    ######################################    Welcome to the Movie Database    ##################################
    #############################################################################################################
""")

# The list where all movies will be stored
movie_list = []


def menu():  # App main menu
    menu_init = input("""
Please choose what you want to do:
A. Add movie
L. List movies
E. Edit movie
R. Remove movie
S. Search for a movie
Q. Exit Movie Database
    
""")

    if menu_init == "A" or menu_init == "a":
        add_movie()  # Run add_movie function
    elif menu_init == "L" or menu_init == "l":
        list_movies()  # Run list_movies function
    elif menu_init == "E" or menu_init == "e":
        edit_movie()  # Run edit_movie function
    elif menu_init == "R" or menu_init == "r":
        remove_movie()  # Run remove_movie function
    elif menu_init == "S" or menu_init == "s":
        pass  # Run search_movie function
    elif menu_init == "Q" or menu_init == "q":
        # Quit application
        print("Application stopped")
        print("\nSee you next time!")
        exit()
    else:  # Wrong input. Rerun app main menu
        print("That is not a valid selection...")
        print("Please try again")
        menu()


def movie_title():
    global title
    title = input("Type in movie title:")
    if title == "":
        print("You need to fill out the movie title...")
        movie_title()
    else:
        return title


def movie_director():
    global director
    director = input("Type in the director of the movie:")
    if director == "":
        print("You need to fill out the director of the movie...")
        movie_director()
    else:
        return director


def release_year():
    global year
    year = int(input("Type in the movie release year:"))
    if year == "":
        print("You need to fill out the year the movie was released...")
        release_year()
    else:
        return year


# Add Movie function
def add_movie():
    movie_title()
    movie_director()
    release_year()
    movie_list.append({
        'title': title,
        'director': director,
        'year': year
    })
    print("Movie added!")
    add_movie_menu = input("""
What would you like to do now?
 
 A. Add another movie
 B. Back to the main menu""")

    if add_movie_menu == "A" or add_movie_menu == "a":
        add_movie()
    else:
        menu()


def list_movies():
    for movie in movie_list:
        list_movie_details(movie)
    menu()


def list_movie_details(movie):
    print(f"""
Name: {movie['title']} 
Director: {movie['director']} 
Release year: {movie['year']}
""")


def edit_movie():
    edit_movie_input = input("Type which movie you want to edit")
    for i in range(len(movie_list)):
        if movie_list[i]['title'] == edit_movie_input:
            print(movie_list[i]['title'], "removed successfully!")
            del movie_list[i]
            menu()
            break


def remove_movie():
    remove_movie_input = input("Type which movie to remove")
    for i in range(len(movie_list)):
        if movie_list[i]['title'] == remove_movie_input:
            print(movie_list[i]['title'], "removed successfully!")
            del movie_list[i]
            menu()
            break


menu()
