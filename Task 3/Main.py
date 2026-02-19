import time
import random
import os

from Entities import characters, enemies


enemy_array = ["goblin", "skeleton", "slime"]                           #list of enemies

#GPTD
class TurnBase:
    def __init__(self, min_turn = 0, max_turn = 100,):
        self.min_turn = min_turn
        self.max_turn = max_turn

    

class Entity:
    def __init__(self,name, health, strenght, defense, attack_speed ) -> None:           #character and enemy statistics
        self.name = name
        self.health = health
        self.strenght = strenght
        self.defense = defense
        self.attack_speed = attack_speed

    def is_alive(self):
        return self.health > 0


class Main:
    def __init__(self):
        self.player = None
        self.enemy = None
        self.logs = []
        self.is_fighting = False

    def enemy_lottery(self):
        enemy_choice = (random.choice(enemy_array))
        enemy = enemies[enemy_choice]


                    # WIP
    def fighting(self, tick):       
        ...

    def render(self):
        print("------Stats------")
        print(f"Player Health: {enemy.health} \t Enemy Health: {}")
        print("-----------------")

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')



    #loading for prettiness
    def loading(self):
        time.sleep(0.5)
        print("loading.")
        time.sleep(0.5)
        print("loading..")
        time.sleep(0.5)
        print("loading...")


    #Choice menu in future inventory/skills/profile cna be added           
    def default_menu(self):
        user_choice = int(input("""Choose your next adventure
        1. Fight
        2. Run
        
        """))
        if user_choice == 1:
            print("You chose to Fight")
            Main.clear()
            Main.loading()
            Main.fighting()
            

        elif user_choice == 2:
            print("you chose to run")

        else:
            print("wrong choice")
            Main.default_menu()
                       
            
    #character menu selection
    def character_menu(self):
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
                    player = Main(**characters["akira"])  
                    Main.default_menu()
                elif user_choice == 2:
                    print("you chose the character Simon")
                    player = Main(**characters["simon"])
                    Main.default_menu()
                elif user_choice == 3:
                    print("you chose the character Igor")
                    player = Main(**characters["igor"])
                    Main.default_menu()
                else:
                    print("wrong choice")
                    Main.character_menu()
            except ValueError:
                ...





Main.enemy_lottery()