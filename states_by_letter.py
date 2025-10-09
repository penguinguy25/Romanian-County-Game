# states by letter
#
# cool
#
#
#
#
#
# uh
#
# im sorry everyone, im too lazy to change the var names.


def states_by_letter_func(the_counties, letter):
    game_counties = set()
    print(f"How many states starting with the letter {letter} can you name ({len(the_counties)} in total)? Type f at any point to give up, type s to see currently guessed states.")
    while True:
        print("Guess a state:")
        county = input("> ")


        # if county guess is correct
        if county.lower() in the_counties and not county.lower() in game_counties:          # lowercased
            game_counties.add(county.lower())               # lowercased
            print(f"State guessed! {len(game_counties)}/{len(the_counties)}")
            if len(game_counties) == len(the_counties):
                print(f"You have won! All US states starting with the letter {letter} have been correctly guessed, {len(game_counties)}/{len(the_counties)}!\nHere's a list of all the states:\n{game_counties}\nBack to the menu . . .\n\n")
                return

        # currently guessed counties    
        elif county.lower() == "s":             # lowercased
            if len(game_counties) == 0:
                print(f"No currently guessed states yet! Type x to exit")
                while True:
                    show_exit = input("> ")
                    if show_exit.lower() == "x":            # lowercased
                        break
                    else:
                        print("That's not a command!")
            else:
                print(f"Currently guessed states:\n{game_counties}\nType x to exit")
                while True:
                    show_exit = input("> ")
                    if show_exit.lower() == "x":            # lowercased
                        break
                    else:
                        print("That's not a command!")


        # if the player gives up
        # press F to pay respects o7
        elif county.lower() == "f":             # lowercased
            print(f"You gave up. You guessed {len(game_counties)}/{len(the_counties)} states.\nHere are the states you didn't guess:\n{the_counties.difference(game_counties)}\n\n")
            return

        # if the county doesnt exist
        elif county.lower() not in the_counties:            # lowercased
            print("That's not a state!")

        
        # if the county was already guessed (else statement as its hopefully the last case possible)
        else:
            print("You have already guessed that state!")