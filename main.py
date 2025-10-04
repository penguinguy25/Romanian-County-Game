# beginning of the romania counties project!
# this is a practice program which was made because i wanted to learn them lol

counties = {"alba", "arad", "arges", "bacau", "bihor", "bistrita-nasaud", "botosani", "brasov", "braila", "buzau",
             "caras-severin", "calarasi", "cluj", "constanta", "covasna", "dambovita", "dolj", "galati", "giurgiu", "gorj",
             "harghita", "hunedoara", "ialomita", "iasi", "ilfov", "maramures", "mehedinti", "mures", "neamt", "olt", "prahova",
             "satu mare", "salaj", "sibiu", "suceava", "teleorman", "timis", "tulcea", "vaslui", "valcea", "vrancea", "bucuresti"}



# counties ^^^ (42)


def all_counties():
    game_counties = set()
    print("All right, start naming as many counties as you can! Type f at any point to give up, type s to see already guessed counties.")
    while True:
        print("Guess a county:")
        county = input("> ")


        # if county guess is correct
        if county.lower() in counties and not county.lower() in game_counties:          # lowercased
            game_counties.add(county.lower())               # lowercased
            print(f"County guessed! {len(game_counties)}/{len(counties)}")
            if len(game_counties) == 42:
                print(f"You have won! All Romanian counties have been correctly guessed, {len(game_counties)}/{len(counties)}!\nHere's a list of all the counties:\n{game_counties}\nBack to the main menu . . .\n\n")
                menu()
                return

        # currently guessed counties    
        elif county.lower() == "s":             # lowercased
            if len(game_counties) == 0:
                print(f"No currently guessed counties yet! Type x to exit")
                while True:
                    show_exit = input("> ")
                    if show_exit.lower() == "x":            # lowercased
                        break
                    else:
                        print("That's not a command!")
            else:
                print(f"Currently guessed counties:\n{game_counties}\nType x to exit")
                while True:
                    show_exit = input("> ")
                    if show_exit.lower() == "x":            # lowercased
                        break
                    else:
                        print("That's not a command!")


        # if the player gives up
        # press F to pay respects o7
        elif county.lower() == "f":             # lowercased
            print(f"You gave up. You guessed {len(game_counties)}/{len(counties)} counties.\nHere are the counties you didn't guess:\n{counties.difference(game_counties)}\n\n")
            menu()
            return

        # if the county doesnt exist
        elif county.lower() not in counties:            # lowercased
            print("That's not a county!")

        
        # if the county was already guessed (else statement as its hopefully the last case possible)
        else:
            print("You have already guessed that county!")
        

# main
def menu():
    print("\nThis is the Romanian county practice game!\nSelect an option:\n1. Play the all-counties naming game\n2. View all the counties")
    while True:
        mode = input("> ")
        if mode == "1":
            all_counties()
            return
        elif mode == "2":
            print(f"Here are all the Romanian counties. You can use this list as a pointer to help you memorize them and win the all-counties naming game!\n\n{counties}\n\nType x to exit")
            while True:
                view_option = input("> ")
                if view_option.lower() == 'x':
                    print("\nThis is the Romanian county practice game!\nSelect an option:\n1. Play the all-counties naming game\n2. View all the counties")          # lowercased
                    break
                else:
                    print("That's not a command!")
        else:
            print("That's not an available option!")
        

menu()
