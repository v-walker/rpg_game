
class Character:
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
        opponent.health -= self.power
        print(f"\nThe {self.name} attacks and does {self.power} damage to {opponent.name}.")
        if opponent.alive == False:
            print(f"\nThe {opponent.name} is dead.")

    def show_stats(self):
        print(f"\nThe {self.name} has {self.health} health and {self.power} power.")

class Hero(Character):
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

def main():

    my_hero = Hero("Hero", 10, 5)
    monsters = []
    goblin = Goblin("Goblin", 6, 2)
    monster = Zombie("Zombie", 15, 2)
    monsters.append(goblin)
    monsters.append(monster)

    print(f"You open the door to the dungeon, and you see {len(monsters)} deadly creatures before you.")
    
    valid_choice = False
    
    # choose an opponent
    while valid_choice == False:
        choice = int(input("""Choose your opponent: 
1. Goblin
2. Zombie
>     """))
        if choice < len(monsters):
            monster = monsters[choice-1]
            valid_choice = True
        else:
            print("Invalid choice. Try again")

    while valid_choice == True and monster.alive() and my_hero.alive():
        my_hero.show_stats()
        monster.show_stats()
        print("")
        select_action = input(f"""What do you want to do?
1. Attack the {monster.name}.
2. Do nothing.
3. Flee for your life!
> """)

        if select_action == "1":
            my_hero.attack(monster)
        elif select_action == "2":
            print("\nYou freeze in terror at the horrible sight of your opponent!")
            pass
        elif select_action == "3":
            print("\nThat was close, but you made it out alive! Maybe stick to smaller monsters for now...")
            break
        else:
            print(f"Invalid input '{select_action}'.")

        if monster.alive() == True:
            monster.attack(my_hero)
        elif monster.alive() == False:
            print(f"\nYou have slain the {monster.name}!")
            print("\n===Game over. You win!===\n")
            break
        
        if my_hero.alive() == False:
            print(f"You are mortally wounded. Too bad you don't know any healers...\n===GAME OVER===\nYOU LOSE\n")
            break

main()