def main():

    print("""
        ########################################################################################################################
        #########################################    Welcome to the Movie Database    ##########################################
        ########################################################################################################################
    """)


def menu():
    menu_init = input("""
Please init what you want to do:
A. Add movie
E. Edit movie
R. Remove movie
S. Search for a movie

Please choose what you want to do...
    
""")

    if menu_init == "A" or menu_init == "a":
        add_movie()
    elif menu_init == "E" or menu_init == "e":
        print("##### Edit movie #####")
    elif menu_init == "R" or menu_init == "r":
        print("##### Remove movie #####")
    elif menu_init == "S" or menu_init == "s":
        print("##### Search for a  movie #####")
    else:
        print("That is not a valid selection...")
        print("Please try again")
        menu()


movies_list = []

# TODO: Split title, director ond year into separat funtions and consolidate in add_movie

def add_movie():
    movie_title = input("Type in movie title:")
    movie_director = input("Type in the director of the movie:")
    release_year = input("Type in the movie release year:")
    movies_list.append({"Movie title": movie_title, "Director": movie_director, "Release date": release_year})
    print(movies_list)
    if movie_title == "":
        print("You need to fill out the movie title")
    elif movie_director == "":
        print("You need to fill out the movie director")
    elif release_year == "":
        print("You need to fill out the movie title")
    else:
        print("Movie added")


menu()
main()
