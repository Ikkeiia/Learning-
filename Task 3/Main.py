import time
import random

from Entities import characters, enemies



enemy_array = ["goblin", "skeleton", "slime"]                           #list of enemies

class CharacterStats:
    
    
    def __init__(self, health, strenght, defense, attack_speed ) -> None:           #character statistics
        self.health = health
        self.strenght = strenght
        self.defense = defense
        self.attack_speed = attack_speed

    def fighting(self):
        
        ...
        
    
akira = CharacterStats(**characters["akira"])               #unpacking the info.  I dont need to load all of them if the user chooses one of the characters i guess so bound to change
igor = CharacterStats(**characters["igor"])
simon = CharacterStats(**characters["simon"])


skeleton = CharacterStats(**enemies["skeleton"])
slime = CharacterStats(**enemies["slime"])
goblin = CharacterStats(**enemies["goblin"])

#loading for prettiness
def loading():
    time.sleep(0.5)
    print("loading.")
    time.sleep(0.5)
    print("loading..")
    time.sleep(0.5)
    print("loading...")

def fighting():
    Chosen_enemy = (random.choice(enemy_array))
    if Chosen_enemy == goblin:
        pass



fighting()



#character menu selection
def character_menu():
   while True:
        try:
            user_choice = int(input("""
            Choose your character: 
            1. Akira
            2. Simon
            3. Igor
            
            """))    
            if user_choice == 1:
                print("You chose the character Akira")
                Main_character = akira
            elif user_choice == 2:
                print("you chose the character Simon")

            elif user_choice == 3:
                print("you chose the character Igor")
            else:
                print("wrong choice")
                character_menu()
        except ValueError:
            ...


#Choice menu in future inventory/skills/profile cna be added           
def default_menu():
    try:
        user_choice = int(input("""Choose your next adventure
          1. Fight
          2. Run
          
          """))
        if user_choice == 1:
            print("You chose to Fight")
            loading()

        elif user_choice == 2:
            print("you chose the character Simon")

        else:
            print("wrong choice")
            default_menu()
    except ValueError:
            ...

