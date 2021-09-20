import random
import time

class Character:
    coin_bank = 10

    def __init__(self, name, health, power, armor, level, coins, backpack = [], evasion = 0):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.level = level
        self.coins = coins
        self.backpack = backpack
        self.evasion = evasion
        
    def alive(self):
        life = True
        if self.health <= 0:
            life = False
        return life

    def default_attack(self, opponent):
        armored_damage = self.power - opponent.armor
        opponent.health -= armored_damage
        print(f"\nThe {self.name} attacks and does {self.power} damage to {opponent.name}.")

    def dodged_attack(self, opponent):
        print(f"\n{opponent.name} dodged {self.name}'s attack!")

    def critical_attack(self, opponent):
        num = random.randint(1, 5)
        if num == 1:
            opponent.health -= (self.power * 2)
        else: self.default_attack(opponent)
        print(f"\nThe {self.name} attacks and does {self.power * 2} damage to {opponent.name}.")

    def attack(self, opponent):
        if opponent.name == "Shadow" or opponent.evasion >= 33:
            num = random.randint(1, 10)
            if num >= 2:
                self.dodged_attack(opponent)
            else:
                if self.name == "Paladin":
                    self.critical_attack(opponent)
                else:
                    self.default_attack(opponent)
        elif opponent.evasion >= 18:
            num = random.randint(1, 2)
            if num == 1:
                opponent.dodged_attack(opponent)
            else:
                if self.name == "Paladin":
                    self.critical_attack(opponent)
                else:
                    self.default_attack(opponent)
        elif opponent.evasion >= 14:
            num = random.randint(1, 5)
            if num < 3:
                self.dodged_attack(opponent)
            else:
                if self.name == "Paladin":
                    self.critical_attack(opponent)
                else:
                    self.default_attack(opponent) 
        elif opponent.name == "Vampire" or (opponent.evasion >= 10 and opponent.evasion <= 11):
            num = random.randint(1, 3)
            if num == 1:
                opponent.health -= round(self.power/2)
                print(f"\nThe {self.name} attacks and does {self.power} damage to {opponent.name}.")
            elif num == 2:
                self.default_attack(opponent)
            else:
                self.dodged_attack(opponent)
        elif opponent.evasion >= 10:
            num = random.randint(1, 3)
            if num == 1:
                self.dodged_attack(opponent)
            else:
                if self.name == "Paladin":
                    self.critical_attack(opponent)
                else:
                    self.default_attack(opponent)
        elif opponent.evasion >= 6:
            num = random.randint(1, 5)
            if num == 1:
                self.dodged_attack(opponent)
            else:
                if self.name == "Paladin":
                    self.critical_attack(opponent)
                else:
                    self.default_attack(opponent)
        elif opponent.evasion >= 2:
            num = random.randint(1, 10)
            if num == 1:
                self.dodged_attack(opponent)
            else:
                if self.name == "Paladin":
                    self.critical_attack(opponent)
                else:
                    self.default_attack(opponent)
        else:
            if self.name == "Paladin":
                    self.critical_attack(opponent)
            else:
                self.default_attack(opponent)
        
        if opponent.alive == False:
            print(f"\nThe {opponent.name} is dead.")

    def show_base_stats(self):
        print(f"\nThe {self.name} has {self.health} health and {self.power} power.")
    
    def show_all_stats(self):
        print(f"\nThe {self.name} has {self.health} health and {self.power} power.")
        print(f"\nYou are currently level {self.level}. You have {self.coins} coins, {self.armor} armor points, and {self.evasion} evasion points.")

    def show_level_coins(self):
        print(f"You are currently level {self.level}, and you have {self.coins} coins")

    def print_inventory(self):
        index = 1
        if len(self.backpack) == 0:
            print("You currently have no items.")
        else:
            print("\nHere is a list of the items you are currently carrying: ")
            for x in self.backpack:
                print(f"{index}: {x.name}")
                index += 1

    def use_item(self, item_obj):
        if item_obj.name == "Super Tonic":
            self.restore_health(10)
        elif item_obj.name == "Armor":
            self.armor_up()
        elif item_obj.name == "Evade":
            self.inc_evade(2)
        elif item_obj.name == "Really Cool Hat":
            print("That's a nice hat you've got there! I wish I had one... \nYou seem a little more evasive while wearing that!")
            self.inc_evade(0.5)
        elif item_obj.name == "Super-Mega Tonic":
            self.restore_health(50)

    def choose_action(self):
        make_choice = True
        while make_choice == True:
            print("""\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    What would you like to do?:

    1. Fight a monster
    2. View my items
    3. Buy an item
    4. Use an item
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n""")

            choice = int(input("> "))

            if choice == 1:
                print("Okay, let's fight!")
                make_choice = False
                return make_choice
            elif choice == 2:
                self.print_inventory()
            elif choice == 3:
                print("Let's head to the town store!")
                time.sleep(1.5)
                self.buy_item()
            elif choice == 4 and len(self.backpack) == 0:
                print("\nSorry, you do not have any items. You can buy items at the store.")
            elif choice == 4 and len(self.backpack) > 0:
                print("Which item would you like to choose?: ")
                self.print_inventory()
                print("\nEnter the number of the item you wish to use.")
                item_choice = (int(input("> ")) - 1)
                if item_choice <= len(self.backpack):
                    item_obj = self.backpack[item_choice]
                    print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nYou have chosen to use {item_obj.name}.")
                    self.use_item(item_obj)
                    del self.backpack[item_choice]
                else:
                    print("Invalid input. Try again.")

    def restore_health(self, power):
        self.health += power
        print("Your health has increased by ten points!")
        self.show_base_stats()

    def armor_up(self):
        self.armor += 2
        print("Your armor has increased by two!")
        self.show_all_stats()

    # Build this out -- need to add evasion points to characters
    def inc_evade(self, power):
        self.evasion += power
        print(f"Your evasion points have increased by {power}!")
        self.show_all_stats()

    def add_item(self, special_item):
            self.coins -= special_item.cost
            self.backpack.append(special_item)
            print(f"\nSuccess!\n{special_item.name} has been added to your backpack!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            item_choice = True
            return item_choice

    def buy_item(self):
        item_choice = False
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nWelcome to the Item Shop. We have many great things here to help you out on your journey!")
        time.sleep(1)
        print("Feel free to take a look around and let us know if you want to buy anything!")
        while item_choice == False:
            choice = int(input("""\nChoose an item (enter the number of the item you wish to purchase)

        Item:             Description:                    Cost:

    1. Super Tonic       increase health                  10 coins
    2. Armor             increase resistance to damage    15 coins
    3. Evade             increase dodge probability       7 coins
    4. Really Cool Hat   you will look awesome            5 coins
    5. Super-Mega Tonic  increase health by a LOT         40 coins
    
    6. Or press 6 to exit shop
    """))
            if choice == 1 and self.coins >= 10:
                special_item = Item("Super Tonic", 10)
                self.add_item(special_item)
            elif choice == 2 and self.coins >= 15:
                special_item = Item("Armor", 15)
                self.add_item(special_item)
            elif choice == 3 and self.coins >= 7:
                special_item = Item("Evade", 7)
                self.add_item(special_item)
            elif choice == 4 and self.coins >= 5:
                special_item = Item("Really Cool Hat", 5)
                self.add_item(special_item)
            elif choice == 5 and self.coins >= 0:
                special_item = Item("Super-Mega Tonic", 40)
                self.add_item(special_item)
            elif choice == 6:
                print("\nThanks for visiting. See you next time!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                item_choice = True
            else:
                print(f"\nThat is not a valid choice. You have {self.coins} coins. Try again.")

class Hero(Character):
    def __init__(self, name, health, power, armor, level, coins, backpack, evasion):
        super().__init__(name, health, power, armor, level, coins, backpack, evasion)
        
class Medic(Character):
    def __init__(self, name, health, power, armor, level, coins, backpack, evasion):
        super().__init__(name, health, power, armor, level, coins, backpack, evasion)
    
    def recuperate_health(self):
        num = random.randint(1, 5)
        if num == 1:
            self.health += 2
            print("\nOh... What's this??")
            time.sleep(0.5)
            print(f"\nThe gods have blessed you with the gift of health! Your health has increased by 2.\nYour Current Health: {self.health}")

class Shadow(Character):
    def __init__(self, name, health, power, armor, level, coins, backpack, evasion):
        super().__init__(name, health, power, armor, level, coins, backpack, evasion)

class Goblin(Character):
    def __init__(self, name, health, power, armor, level, coins, backpack, evasion):
        super().__init__(name, health, power, armor, level, coins, backpack, evasion)

class Zombie(Character):
    def __init__(self, name, health, power, armor, level, coins, backpack):
        super().__init__(name, health, power, armor, level, coins, backpack)

    def alive(self):
        revived_health = 15
        life = True
        if self.health <= 0:
            time.sleep(0.75)
            print(f"You land a fatal blow, and the {self.name} falls to the ground.")
            time.sleep(0.75)
            print("...")
            time.sleep(0.75)
            print("...")
            time.sleep(0.75)
            print("...")
            time.sleep(0.75)
            print(f"Oh no! The {self.name} regains its health!")
            time.sleep(0.75)
            print("It's getting back up!")
            self.health += revived_health
            time.sleep(0.75)
        return life

class Vampire(Character):
    def __init__(self, name, health, power, armor, level, coins, backpack, evasion):
        super().__init__(name, health, power, armor, level, coins, backpack, evasion)

class Bugbear(Character):
    def __init__(self, name, health, power, armor, level, coins, backpack, helper, evasion):
        super().__init__(name, health, power, armor, level, coins, backpack, evasion)
        self.helper = helper

    def attack(self, opponent):
        num = random.randint(1, 5)
        if num == 1:
            self.power += self.helper.power
            opponent.health -= self.power
            print(f"\nThe {self.name} attacks along with a goblin and does {self.power} damage to {opponent.name}.")
        else:
            opponent.health -= self.power
            print(f"\nThe {self.name} attacks and does {self.power} damage to {opponent.name}.")
        if opponent.alive == False:
            print(f"\nThe {opponent.name} is dead.")


class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

def invalid_choice():
    print("Invalid choice. Try again.")


def choose_player_char():
    char_choice = False
    while char_choice == False:
        choice = int(input("""\nChoose your player character:
1. Paladin
2. Dwarf Cleric
3. Shadow
>     """))
        if choice == 1:
            player_char = Hero("Paladin", 10, 5, 0, 1, 15, [], 0)
            char_choice = True
        elif choice == 2:
            player_char = Medic("Dwarf Cleric", 10, 4, 0.5, 1, 15, [], 10)
            char_choice = True
        elif choice == 3:
            player_char = Shadow("Shadow", 1, 6, 0, 1, 15, [], 33)
            char_choice = True
        else: 
            invalid_choice()
    print(f"\nYou chose {player_char.name}. Your character is currently level {player_char.level}. You currently have {player_char.coins} coins. \nLet's go!!!")
    return player_char

def choose_opponent():
    opp_choice = False
    while opp_choice == False:
        choice = int(input("""\nChoose your opponent: 
1. Goblin
2. Zombie
3. Vampire
4. Bugbear
>     """))
        if choice == 1:
            monster = Goblin("Goblin", 6, 2, 0, 1, 5, [], 2)
            opp_choice = True
        elif choice == 2:
            monster = Zombie("Zombie", 15, 1, 0, 1, 10, [], 2)
            opp_choice = True
        elif choice == 3:
            monster = Vampire("Vampire", 20, 4, 0, 1, 6, [], 2)
            opp_choice = True
        elif choice == 4:
            monster = Bugbear("Bugbear", 18, 3, 0, 1, 8, [], 2, Goblin("Goblin", 6, 2, 5))
            opp_choice = True
        else:
            invalid_choice()
    return monster



def main():

    print("\nAre you ready for an adventure?")
    time.sleep(1.5)
    print("I hope the answer was 'yes' because heeeeeeere we go!")
    time.sleep(0.5)
    print("\nLet's start with choosing a player character!")

    #Choose a player character
    player_char = choose_player_char()
    play_again = True
    while play_again == True:
    
        if player_char.level > 1:
            player_char.show_all_stats()
        
        player_char.choose_action()
        
        # choose an opponent
        monster = choose_opponent()
        if player_char.level > 1:
                monster.power += player_char.level/2
        else:
            monster.power += 0
        
        while monster.alive() and player_char.alive():
            player_char.show_base_stats()
            
            monster.show_base_stats()
            print("")
            select_action = input(f"""\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    What do you want to do?

    1. Attack the {monster.name}.
    2. Do nothing.
    3. Flee for your life!
    4. Use an item.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    > """)

            if select_action == "1":
                player_char.attack(monster)
            elif select_action == "2":
                print("\nYou freeze in terror at the horrible sight of your opponent!")
                pass
            elif select_action == "3":
                print("\nThat was close, but you made it out alive! Maybe stick to smaller monsters for now...")
                break
            # Add in action 4 "Use an item"
            else:
                print(f"Invalid input '{select_action}'.")

            if monster.alive() == True:
                monster.attack(player_char)
            
            if player_char.name == "Medic":
                player_char.recuperate_health()

            elif monster.alive() == False:
                print(f"\nYou have slain the {monster.name}!")
                player_char.coins += monster.coins
                print(f"\nThe town's folk would like to thank you for your service. You collect {monster.coins} coins.\nYou now have {player_char.coins} coins.")
                play_again = False
                while play_again == False:
                    time.sleep(1.5)
                    next_monster = input("\nWould you like to continue your adventure? Enter 'y' for 'yes' or 'n' to exit the game: ")
                    if next_monster == "y":
                        player_char.level += 1
                        play_again = True
                    
                    elif next_monster == "n":
                        print("\nThanks for playing!\nSee if you can reach a higher level next time!\n===Game Over===\n")
                        break
                    else:
                        invalid_choice()

            if player_char.alive() == False:
                print("\nYou are mortally wounded. Too bad you don't know anyone who can revive you...\n\n=====GAME OVER===\n\n=====YOU LOSE=====\n")
                play_again = False
                break

main()