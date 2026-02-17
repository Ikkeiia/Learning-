import time
import random

from Entities import characters, enemies



enemy_array = ["goblin", "skeleton", "slime"]                           #list of enemies

class main:

    class TickBase:
       
        def __init__(self, tick_rate=64):
            self.tick_rate = tick_rate
            self.tick_interval = 1.0 / tick_rate  # Seconds per tick
            
            self.current_tick = 0
            self.start_time = time.perf_counter()
            self.accumulator = 0.0
            self.last_time = self.start_time
            



        def update(self, callback):
            """
            Calculates elapsed time and runs the callback 
            for every tick that should have occurred.
            """
            now = time.perf_counter()
            frame_time = now - self.last_time
            self.last_time = now
            
            # Add the time passed since the last frame to our 'bank'
            self.accumulator += frame_time

            # If we have enough 'banked' time for one or more ticks, run them
            while self.accumulator >= self.tick_interval:
                self.current_tick += 1
                callback(self.current_tick)
                self.accumulator -= self.tick_interval


    class player:
        
        
        def __init__(self, health, strenght, defense, attack_speed ) -> None:           #character statistics
            self.health = health
            self.strenght = strenght
            self.defense = defense
            self.attack_speed = attack_speed

        def is_alive(self):
            return self.health > 0
        
        
                #unpacking the info.  I dont need to load all of them if the user chooses one of the characters i guess so bound to change
        def fighting(self,):
            enemy = (random.choice(enemy_array))

            





    #loading for prettiness
        def loading():
            time.sleep(0.5)
            print("loading.")
            time.sleep(0.5)
            print("loading..")
            time.sleep(0.5)
            print("loading...")


    #Choice menu in future inventory/skills/profile cna be added           
        def default_menu():
            user_choice = int(input("""Choose your next adventure
            1. Fight
            2. Run
            
            """))
            if user_choice == 1:
                print("You chose to Fight")
                main.player.loading()
                main.player.fighting()
                

            elif user_choice == 2:
                print("you chose to run")

            else:
                print("wrong choice")
                main.player.default_menu()
                       
            



  



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
                        player = main.player(**characters["akira"])  
                        main.player.default_menu()
                    elif user_choice == 2:
                        print("you chose the character Simon")
                        player = main.player(**characters["simon"])
                        main.player.default_menu()
                    elif user_choice == 3:
                        print("you chose the character Igor")
                        player = main.player(**characters["igor"])
                        main.player.default_menu()
                    else:
                        print("wrong choice")
                        main.player.character_menu()
                except ValueError:
                    ...





main.player.character_menu()