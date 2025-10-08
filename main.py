# beginning of the romania counties project!
# this is a practice program which was made because i wanted to learn them lol
from counties_by_letter import counties_by_letter_func



counties = {"alba", "arad", "arges", "bacau", "bihor", "bistrita-nasaud", "botosani", "brasov", "braila", "buzau",
             "caras-severin", "calarasi", "cluj", "constanta", "covasna", "dambovita", "dolj", "galati", "giurgiu", "gorj",
             "harghita", "hunedoara", "ialomita", "iasi", "ilfov", "maramures", "mehedinti", "mures", "neamt", "olt", "prahova",
             "satu mare", "salaj", "sibiu", "suceava", "teleorman", "timis", "tulcea", "vaslui", "valcea", "vrancea", "bucuresti"}



# counties ^^^ (42)


def all_counties():
    game_counties = set()
    print("All right, start naming as many counties as you can! Type f at any point to give up, type s to see currently guessed counties.")
    while True:
        print("Guess a county:")
        county = input("> ")


        # if county guess is correct
        if county.lower() in counties and not county.lower() in game_counties:          # lowercased
            game_counties.add(county.lower())               # lowercased
            print(f"County guessed! {len(game_counties)}/{len(counties)}")
            if len(game_counties) == 42:
                print(f"You have won! All Romanian counties have been correctly guessed, {len(game_counties)}/{len(counties)}!\nHere's a list of all the counties:\n{game_counties}\nBack to the main menu . . .\n\n")
                return
                # FIXME
                # removed menu() here and left return

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
            return
            # FIXME
            # removed menu() here too and left return

        # if the county doesnt exist
        elif county.lower() not in counties:            # lowercased
            print("That's not a county!")

        
        # if the county was already guessed (else statement as its hopefully the last case possible)
        else:
            print("You have already guessed that county!")
        




# FIXME
# ^^ this is because my idiotic ahh forgot bucuresti as a county :broken_heart: and i cba to fix it now





# FIXME
# counties by letter minigame









# main counties by letter menu
# counties by letter list
b_counties = {"bacau", "bihor", "bistrita-nasaud", "botosani", "brasov", "braila", "buzau", "bucuresti"}
c_counties = {"caras-severin", "calarasi", "cluj", "constanta", "covasna"}
a_counties = {"alba", "arad", "arges"}
d_counties = {"dambovita", "dolj"}
g_counties = {"galati", "giurgiu", "gorj"}
h_counties = {"harghita", "hunedoara"}
i_counties = {"ialomita", "iasi", "ilfov"}
m_counties = {"maramures", "mehedinti", "mures"}
n_counties = {"neamt"}
o_counties = {"olt"}
p_counties = {"prahova"}
s_counties = {"satu mare", "salaj", "sibiu", "suceava"}
t_counties = {"teleorman", "timis", "tulcea"}
v_counties = {"vaslui", "valcea", "vrancea"}




def counties_by_letter():
    # added the print statement to the while loop for smooth func recalling
    # FIXME just in case
    while True:
        print("Welcome to Counties by Letter! Currently we will only include the letters that a majority of the counties start with. Select a mode below or type x to exit:")
        print("1. A (3 counties)   8. M (3 counties)")
        print("2. B (8 counties)   9. N (1 county)")
        print("3. C (5 counties)   10. O (1 county)")
        print("4. D (2 counties)   11. P (1 county)")
        print("5. G (3 counties)   12. S (4 counties)")
        print("6. H (2 counties)   13. T (3 counties)")
        print("7. I (3 counties)   14. V (3 counties)")
        letter = input("> ")
        if letter == "x":
            menu()
            return
        elif letter == "1":
            counties_by_letter_func(a_counties, "A")
        elif letter == "2":
            counties_by_letter_func(b_counties, "B")
        elif letter == "3":
            counties_by_letter_func(c_counties, "C")
        elif letter == "4":
            counties_by_letter_func(d_counties, "D")
        elif letter == "5":
            counties_by_letter_func(g_counties, "G")
        elif letter == "6":
            counties_by_letter_func(h_counties, "H")
        elif letter == "7":
            counties_by_letter_func(i_counties, "I")
        elif letter == "8":
            counties_by_letter_func(m_counties, "M")
        elif letter == "9":
            counties_by_letter_func(n_counties, "N")
        elif letter == "10":
            counties_by_letter_func(o_counties, "O")
        elif letter == "11":
            counties_by_letter_func(p_counties, "P")
        elif letter == "12":
            counties_by_letter_func(s_counties, "S")
        elif letter == "13":
            counties_by_letter_func(t_counties, "T")
        elif letter == "14":
            counties_by_letter_func(v_counties, "V")
        else:
            print("That's not an available option!")







# main
def menu():
    # added print to the while true loop for smooth func recalling and stuff
    # FIXME
    # ^^ jst in case
    while True:
        print("\nThis is the Romanian county practice game!\nSelect an option:\n1. Play the all-counties naming game\n2. View all the counties\n3. Counties by Letter")
        mode = input("> ")
        if mode == "1":
            all_counties()
        elif mode == "2":
            print(f"Here are all the Romanian counties. You can use this list as a pointer to help you memorize them and win the all-counties naming game!\n\n{counties}\n\nType x to exit")
            while True:
                view_option = input("> ")
                if view_option.lower() == 'x':
                    print("\nThis is the Romanian county practice game!\nSelect an option:\n1. Play the all-counties naming game\n2. View all the counties\n3. Counties by Letter")          # lowercased
                    break
                else:
                    print("That's not a command!")
        elif mode == "3":
            counties_by_letter()

        else:
            print("That's not an available option!")
        

menu()
