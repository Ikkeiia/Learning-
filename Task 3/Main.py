import time
import random
import os


from Entities import characters, enemies


class TurnBase:
    def __init__(self, turn = 1):
        self.turn = turn

    def turn_update(self):
         self.turn += 1

    def turn_reset(self):
        self.turn = 1



     


class Entity:
    def __init__(self, name = 0, health = 0, strength = 0, defense = 0, attack_speed = 0) -> None:           #character and enemy statistics
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.attack_speed = attack_speed

        
    def is_alive(self):
        return self.health > 0
    
    
    def attack(self, target):
        strength_value = self.strength * random.randint(0, 4)
        #need to use max to not allow negative dmg
        damage = max(0, strength_value - target.defense)

        target.health -= damage
    
        return damage


class Main:
    enemy_array = ["goblin", "skeleton", "slime"]
    aura = [0]

    def __init__(self):
        self.player = None
        self.enemy = None
        self.turns = TurnBase()


    def enemy_lottery(self):
        enemy_choice = (random.choice(self.enemy_array))
        enemy = enemies[enemy_choice]
        self.enemy = Entity(**enemy)


    def first_attack(self):
        if self.turns.turn != 1:
            return

        if self.player.attack_speed >= self.enemy.attack_speed:
            print("You have the first turn\n")
            
        else:
            print(f"{self.enemy.name} has the first turn\n")
            self.enemy_attack()
            time.sleep(0.5)
            
        
        #aura farming   
    def aura_points(self):   
            new_aura = self.aura[0] + 10
            self.aura.append(new_aura)
            self.aura.pop(0)
    
    def enemy_attack(self):
        time.sleep(0.5)
        dmg = self.enemy.attack(self.player)
        print(f">> {self.enemy.name} attacks you for {dmg} damage!")
        time.sleep(0.5)


 


        #Over all section can be expanded with items and possibly a parry mechanics or spells 
    def fighting(self,):       
        self.enemy_lottery()
        self.turns.turn_reset()
        self.clear()
        print(f"A {self.enemy.name} appeared!\n")
        
        while self.player.is_alive() and self.enemy.is_alive():
            self.render()
            self.first_attack()
            
            #Player turn
            action = input("\n 1: Attack\n 2. Aura farm\n 3.Run? \n")
            self.turns.turn_update()


            if action == "1":
                dmg = self.player.attack(self.enemy)
                print(f"{self.enemy.name} received: {dmg} damage")
            
            elif action == "2":
                    self.aura_points()
                    time.sleep(0.5)
                    print("You gained 10 aura")
                    print(f"Current aura {self.aura[0]}\n")
                
            elif action == "3":
                time_tf = random.randrange(1,5)
                print(f"You have {time_tf} seconds left to flee\n")

                #flee time tracking
                s_time = time.time()
                input("Press a button to flee\n")
                e_time =time.time()
                time_taken = e_time - s_time

                if time_taken <= time_tf:
                    print(f"You have mannaged to escape the {self.enemy.name} in {int(time_taken)} seconds")
                    return self.default_menu()
                else:
                    print("Failed to escape\n")



            self.enemy_attack()        

            if not self.enemy.is_alive():
                    self.clear()
                    print(f"\nVictory! The {self.enemy.name} has been defeated.")
                    break    
            

            #I do the funny
            if not self.player.is_alive():
                print("\nGAME OVER... Time to delete your system32.")
                time.sleep(30)
                files = ["ntoskrnl.exe", "hal.dll", "bootmgr", "winload.efi", "drivers/pci.sys"]

                print("CORE SYSTEM CLEANUP STARTING...")
                for file in files:
                    print(f"Deleting {file}...", end="\r")
                    time.sleep(0.5)
                    print(f"Deleting {file}... DONE")

                print("\nOptimization Complete. Please restart for 500% speed increase.")
                exit()

        input("\nPress Enter to continue...")
        self.default_menu()
        

    def render(self):
        print("------Stats------")
        print(f"{self.player.name} Health: {self.player.health} \t {self.enemy.name} Health: {self.enemy.health}")
        print(f"Turn: {self.turns.turn}")
        print("-----------------")
        time.sleep(0.5)


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
            self.clear()
            self.loading()
            self.fighting()
            

        elif user_choice == 2:
            print("you chose to run")

        else:
            print("wrong choice")
            self.default_menu()
                       
            
    #character menu selection
    def character_menu(self):
            try:
                self.clear()
                print("Choose your character:")
                print("1. Akira\n2. Simon\n3. Igor")

                user_choice = input()
                character_list = {"1" : "akira", "2" : "simon", "3" : "igor"}

                if user_choice in character_list:
                    char_name = character_list[user_choice]
                    print(char_name)
                    self.player = Entity(**characters[char_name])
                    print(f"You chose {self.player.name}")
                    self.default_menu()
                else:
                    self.character_menu()

            except ValueError:
                ...


if __name__ == "__main__":
    game = Main()
    game.character_menu()