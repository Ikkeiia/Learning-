import time
import random
import os

from Entities import characters, enemies


enemy_array = ["goblin", "skeleton", "slime"]                           #list of enemies

#GPTD
class TickBase:
    def __init__(self, tick_rate=32):
        self.tick_interval = 1.0 / tick_rate
        self.accumulator = 0.0
        self.last_time = time.perf_counter()
        self.current_tick = 0

    def update(self, callback):
        now = time.perf_counter()
        self.accumulator += now - self.last_time
        self.last_time = now

        while self.accumulator >= self.tick_interval:
            self.current_tick += 1
            callback(self.current_tick)
            self.accumulator -= self.tick_interval

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
        self.tickbase = TickBase(tick_rate=32)
        self.player = None
        self.enemy = None
        self.logs = []
        self.is_fighting = False

    def enemy_lottery(self):
        enemy_choice = (random.choice(enemy_array))
        data = enemies[enemy_choice]


                    # WIP
    def fighting(self, tick):       
        ...

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
                    player = Main.Entity(**characters["simon"])
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





Main.character_menu()