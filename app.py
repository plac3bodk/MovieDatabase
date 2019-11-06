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
        print("##### Add movie #####")
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


menu()




