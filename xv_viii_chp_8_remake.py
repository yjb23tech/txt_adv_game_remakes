class BroadSword:
    def __init__(self):
        self.str_name = "Broad Sword"
        self.str_description = "perfect for close to close combat with a large area of effect when sieged by multiple foes"
        self.int_damage = 100

    def __str__(self):
        return (f"This is your {self.str_name} and it is {self.str_description} with an attack strength of {self.int_damage}")

class CrossBow:
    def __init__(self, str_nickname):
        self.str_name = "Cross Bow"
        self.str_nickname = str_nickname
        self.str_description = "perfect for long distance enemies; pick them off at will"
        self.int_damage = 50

    def __str__(self):
        return (f"This is your {self.str_name} which you have nicknamed the {self.str_nickname}; it is {self.str_description} with an attack damage of {self.int_damage}")

arr_action_options = ['N to travel North', 'E to travel East', 'S to travel South', 'W to travel West', 'I to access your Inventory', 'Q to save and Quit the game']

#Used an explicit param declaration here for the single argument param to be passed in to override positional param passing; make it EXPLICIT
arr_inventory_items = ['Crusty Bread', BroadSword(), CrossBow(str_nickname = "Flying God of Death"), 'Gauntlets', 'Healing Potion'] 

def get_user_input():

    return input(f"\nWhat would you like to do Captain?\n")

def play():

    bool_game_is_on = True 

    print("\nYahargh matey! Welcome to the Grand Line :D let's set sail!\n")

    while (bool_game_is_on):

        print("You can choose from the following options:\n")
        option_counter = 1
        for option in arr_action_options:
            print(f"{option_counter}. Press {option}")
            option_counter += 1

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

            print(" ")
        elif player_ui in ['Quit', 'QUIT', 'quit', 'Q', 'q']:
            player_ui = input("You have chosen to quit; are you sure this is your desired option? Type Q-U-I-T to save and quit the game, Captain\n")
            if player_ui.upper() == 'QUIT':
                print("\nThe ship has been docked and you may exit starborn; we will meet again, Captain\n")
                bool_game_is_on = False
            else:
                print("Well shiver me timbers! I was worried you might be a lily livered fella for a second! Back to the ship we go XD\n")
                
        else:
            print("Try again Captain!\n")

    print("Thank you for playing :D")

play()
                 

