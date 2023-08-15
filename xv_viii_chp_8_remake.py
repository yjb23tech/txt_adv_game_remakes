arr_action_options = ['N to travel North', 'E to travel East', 'S to travel South', 'W to travel West']
arr_inventory_items = ['Crusty Bread', 'Broad Sword', 'Crossbow', 'Gauntlets', 'Healing Potion'] 

def get_user_input():

    return input(f"\nWhat would you like to do Captain?\n")

def play():

    bool_game_is_on = True 

    while (bool_game_is_on):

        player_ui = get_user_input()

        if player_ui in ['North', 'NORTH', 'north', 'N', 'n', '^']:
            print("You're now travelling North!\n")
        elif player_ui in ['East', 'EAST', 'east', 'E', 'e', '>']:
            print("You're now travelling East!\n")
        elif player_ui in ['South', 'SOUTH', 'south', 'S', 's', 'v']:
            print("You're now travelling South!\n")
        elif player_ui in ['West', 'WEST', 'west', 'W', 'w', '<']:
            print("You're now travelling West!\n")
        elif player_ui in ['Inventory', 'INVENTORY', 'inventory', 'I', 'i']:
            print("You have chosen to access your inventory; you have access to the following items:\n")
            for x, item in enumerate(arr_inventory_items, 1):
                print(f"{x}. {item}")

            print("\nChoose an item")
        elif player_ui in ['Quit', 'QUIT', 'quit', 'Q', 'q']:
            player_ui = input("You have chosen to quit; are you sure this is your desired option? Type Q-U-I-T to save and quit the game, Captain\n")
            if player_ui.upper() == 'QUIT':
                print("\nThe ship has been docked and you may exit starborn; we will meet again, Captain\n")
                bool_game_is_on = False
            else:
                print("Well shiver me timbers! I was worried you might be a lily livered fella for a second! Back to the ship we go XD\n")
                
        else:
            print("Try again Captain!")

    print("Thank you for playing :D")

play()
                 

