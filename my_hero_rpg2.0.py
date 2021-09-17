import random


class Character:
    damage = False
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        

    def alive(self):
        life = True
        if self.health <= 0:
            life = False
        return life

    def attack(self, opponent):
        if opponent.name == "Shadow":
            num = random.randint(1, 10)
            if num == 1:
                damage = True
                if damage == True:
                    opponent.health -= self.power
                    print(f"\nThe {self.name} attacks and does {self.power} damage to {opponent.name}.")
            else:
                opponent.health -= 0
                print(f"\n{opponent.name} dodged {self.name}'s attack!")
        else:
            opponent.health -= self.power
            print(f"\nThe {self.name} attacks and does {self.power} damage to {opponent.name}.")
        if opponent.alive == False:
            print(f"\nThe {opponent.name} is dead.")

    def show_stats(self):
        print(f"\nThe {self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

    def attack(self, opponent):
        num = random.randint(1, 5)
        if num == 1:
            self.power = self.power * 2
        opponent.health -= self.power
        print(f"\nThe {self.name} attacks and does {self.power} damage to {opponent.name}.")
        if opponent.alive == False:
            print(f"\nThe {opponent.name} is dead.")

class Medic(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
    
    def recuperate_health(self):
        num = random.randint(1, 5)
        if num == 1:
            self.health += 2
            print(f"\nOh... What's this??\nThe gods have blessed you with the gift of health! Your health has increased by 2.\nYour Current Health: {self.health}")

class Shadow(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)

class Zombie(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health, power)
        
    def alive(self):
        revived_health = 15
        life = True
        if self.health <= 0:
            print(f"You land a fatal blow, and the {self.name} falls to the ground.")
            print("...")
            print("...")
            print("...")
            print(f"Oh no! The {self.name} regains its health! It's getting back up!")
            self.health += revived_health
        return life

def invalid_choice():
    print("Invalid choice. Try again")

def main():
    player_chars = []
    paladin = Hero("Paladin", 10, 5)
    medic = Medic("Dwarf Cleric", 10, 4)
    shadow = Shadow("Shadow", 1, 5)
    player_chars.append(paladin)
    player_chars.append(medic)
    player_chars.append(shadow)
    
    monsters = []
    goblin = Goblin("Goblin", 6, 2)
    monster = Zombie("Zombie", 15, 2)
    monsters.append(goblin)
    monsters.append(monster)

    print(f"You open the door to the dungeon, and you see {len(monsters)} deadly creatures before you.")
    
    char_choice = False
    
    while char_choice == False:
        choice = int(input("""\nChoose your player character:
1. Paladin
2. Medic
3. Shadow
>     """))
        if char_choice <= len(player_chars) and choice >= 0:
            player_char = player_chars[choice - 1]
            char_choice = True
        else: 
            invalid_choice()
    
    opp_choice = False
    # choose an opponent
    while opp_choice == False:
        choice = int(input("""\nChoose your opponent: 
1. Goblin
2. Zombie
>     """))
        if choice <= len(monsters) and choice >= 0:
            monster = monsters[choice - 1]
            opp_choice = True
        else:
            invalid_choice()

    while char_choice == True and opp_choice == True and monster.alive() and player_char.alive():
        player_char.show_stats()
        monster.show_stats()
        print("")
        select_action = input(f"""What do you want to do?
1. Attack the {monster.name}.
2. Do nothing.
3. Flee for your life!
> """)

        if select_action == "1":
            player_char.attack(monster)
        elif select_action == "2":
            print("\nYou freeze in terror at the horrible sight of your opponent!")
            pass
        elif select_action == "3":
            print("\nThat was close, but you made it out alive! Maybe stick to smaller monsters for now...")
            break
        else:
            print(f"Invalid input '{select_action}'.")

        if monster.alive() == True:
            monster.attack(player_char)
        
        if player_char.name == "Medic":
            player_char.recuperate_health()

        elif monster.alive() == False:
            print(f"\nYou have slain the {monster.name}!")
            print("\n===Game over. You win!===\n")
            break
        
        if player_char.alive() == False:
            print("\nYou are mortally wounded. Too bad you don't know anyone who can revive you...\n\n===GAME OVER===\n\nYOU LOSE\n")
            break

main()