def add_movie():
    # movie_title = input("Type in movie title:")
    movie_director = input("Type in the director of the movie:")
    release_year = input("Type in the movie release year:")
    movies_list.append({"Movie title": movie_title, "Director": movie_director, "Release date": release_year}, )
    print(movies_list)
    if movie_title == "":
        print("You need to fill out the movie title")
    elif movie_director == "":
        print("You need to fill out the movie director")
    elif release_year == "":
        print("You need to fill out the movie title")
    else:
        print("Movie added")
        add_movie_menu = input("""
What would you like to do now?

 A. Add another movie
 B. Back to the main menu""")