import time
import random
import os

from Entities import characters, enemies


     


class Entity:
    def __init__(self, name, health, strength, defense, attack_speed) -> None:           #character and enemy statistics
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.attack_speed = attack_speed


    def is_alive(self):
        return self.health > 0
    
    
    def attack(self, target):

        damage = self.strength * 2 - (target.defense)
        target.health -= damage
        return damage


class Main:
    enemy_array = ["goblin", "skeleton", "slime"]
    aura = [0]

    def __init__(self):
        self.player = None
        self.enemy = None


    def enemy_lottery(self):
        enemy_choice = (random.choice(self.enemy_array))
        enemy = enemies[enemy_choice]
        self.enemy = Entity(**enemy)

    def first_attack(self):
        if self.player.attack_speed >= self.enemy.attack_speed:
            ...
            
        else:
            self.enemy_attack()
        
    def aura_points(self):
            try:       
                new_aura = self.aura[0] + 10
                self.aura.append(new_aura)
                self.aura.pop(0)
            except IndexError:
                ...


                    # WIP
    def fighting(self):       
        self.enemy_lottery()
        self.clear()
        print(f"A wild {self.enemy.name} appeared!\n")
        
        while self.player.is_alive() and self.enemy.is_alive():
            
            self.render()
            self.first_attack()
            
            #Player turn
            action = input("\n 1: Attack\n 2. Aura farm\n 3.Run? ")

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
                print(f"you have {time_tf} seconds left to flee")

                s_time = time.time()
                input("Press a button to flee")
                e_time =time.time()
                time_taken = e_time - s_time

                if time_taken <= time_tf:
                    print(f"You have mannaged to eskape the {self.enemy.name} in {time_taken} seconds")
                    return
                else:
                    print("failed to escape")
                    

            if not self.enemy.is_alive():
                    print(f"\nVictory! The {self.enemy.name} has been defeated.")
                    break
            
            self.enemy_attack()

            
            if not self.player.is_alive():
                print("\nGAME OVER... You perished in battle.")
                exit()

        input("\nPress Enter to continue...")
        self.default_menu()


    def enemy_attack(self):
            time.sleep(0.5)
            dmg = self.enemy.attack(self.player)
            print(f">> {self.enemy.name} attacks you for {dmg} damage!")
            time.sleep(0.5)
        



    def render(self):
        print("------Stats------")
        print(f"Player Health: {self.player.health} \t Enemy Health: {self.enemy.health}")
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