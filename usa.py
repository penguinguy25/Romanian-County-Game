# usa states guessing
#
# main.py usa file
#
#
#
# main menu
# 
# yeah!!!!!!!!!!!!!!!!!!!!!!!!
usa_states = {"alabama", "alaska", "arizona", "arkansas",
              "california", "colorado", "connecticut", "delaware",
              "florida", "georgia", "hawaii", "idaho", "illinois",
              "indiana", "iowa", "kansas", "kentucky", "louisiana",
              "maine", "maryland", "massachusetts", "michigan",
              "minnesota", "mississippi", "missouri", "montana",
              "nebraska", "nevada", "new hampshire", "new jersey",
              "new mexico", "new york", "north carolina", "north dakota",
              "ohio", "oklahoma", "oregon", "pennsylvania", "rhode island",
              "south carolina", "south dakota", "tennessee", "texas",
              "utah", "vermont", "virginia", "washington", "west virginia",
              "wisconsin", "wyoming"}
# some function
def view_states():
    print(f"Here are all the US states. You can use this list as a pointer to help you memorize them and win the all-states naming game!\n\n{usa_states}\n\nType x to exit")
    while True:
        view_option = input("> ")
        if view_option.lower() == 'x':
            return
        else:
            print("That's not a command!")




def usa_menu(): 
    while True:
        print("USA states main menu, select a mode or enter x to go back to the main menu")
        print("1. All states guessing game")
        print("2. States by Letter")
        print("3. View all states")

        while True:
        
            choice = input("> ")
            if choice == "1":
                all_states()






def all_states():
    # all main states
    # yes
    # what
    # am
    # i
    # doing
    # with
    # my
    # life?
    



    game_states = set()
    print("All right, start naming as many states as you can! Type f at any point to give up, type s to see currently guessed states.")
    while True:
        print("Guess a state:")
        state = input("> ")


        # if county guess is correct
        if state.lower() in usa_states and not state.lower() in game_states:          # lowercased
            game_states.add(state.lower())               # lowercased
            print(f"County guessed! {len(game_states)}/{len(usa_states)}")
            if len(game_states) == 50:
                print(f"You have won! All USA states been correctly guessed, {len(game_states)}/{len(usa_states)}!\nHere's a list of all the states:\n{game_states}\nBack to the main menu . . .\n\n")
                return
                # FIXME
                # removed menu() here and left return

        # currently guessed counties    
        elif state.lower() == "s":             # lowercased
            if len(game_states) == 0:
                print(f"No currently guessed states yet! Type x to exit")
                while True:
                    show_exit = input("> ")
                    if show_exit.lower() == "x":            # lowercased
                        break
                    else:
                        print("That's not a command!")
            else:
                print(f"Currently guessed states:\n{game_states}\nType x to exit")
                while True:
                    show_exit = input("> ")
                    if show_exit.lower() == "x":            # lowercased
                        break
                    else:
                        print("That's not a command!")


        # if the player gives up
        # press F to pay respects o7
        elif state.lower() == "f":             # lowercased
            print(f"You gave up. You guessed {len(game_states)}/{len(usa_states)} states.\nHere are the states you didn't guess:\n{usa_states.difference(game_states)}\n\n")
            return
            # FIXME
            # removed menu() here too and left return

        # if the county doesnt exist
        elif state.lower() not in usa_states:            # lowercased
            print("That's not a state!")

        
        # if the county was already guessed (else statement as its hopefully the last case possible)
        else:
            print("You have already guessed that state!")
