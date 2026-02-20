import time
import random
import os
import sys

# Assume these are imported correctly from your files
# from Entities import characters, enemies
characters = {"akira": {"health": 100, "strength": 10, "defense": 5, "attack_speed": 10}}
enemies = {"goblin": {"health": 50, "strength": 5, "defense": 2, "attack_speed": 32}}
enemy_array = ["goblin"]

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
    def __init__(self, name, health, strength, defense, attack_speed):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.attack_speed = attack_speed

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.tickbase = TickBase(tick_rate=32)
        self.player = None
        self.enemy = None
        self.logs = []
        self.is_fighting = False

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def spawn_enemy(self):
        e_type = random.choice(enemy_array)
        data = enemies[e_type]
        self.enemy = Entity(e_type, data['health'], data['strength'], data['defense'], data['attack_speed'])
        self.logs.append(f"A wild {e_type} appeared!")

    def combat_tick(self, tick):
        """This is the callback function for TickBase"""
        if not self.is_fighting: return

        # Enemy attacks every 'attack_speed' ticks
        if tick % self.enemy.attack_speed == 0:
            dmg = max(1, self.enemy.strength - self.player.defense)
            self.player.health -= dmg
            self.logs.append(f"[{tick}] {self.enemy.name} hit you for {dmg}!")

        # Player attacks every 20 ticks (fixed for example)
        if tick % 20 == 0:
            dmg = max(1, self.player.strength - self.enemy.defense)
            self.enemy.health -= dmg
            self.logs.append(f"[{tick}] You hit {self.enemy.name} for {dmg}!")

        if not self.enemy.is_alive() or not self.player.is_alive():
            self.is_fighting = False

    def render(self):
        self.clear()
        print(f"--- TICK: {self.tickbase.current_tick} ---")
        print(f"PLAYER: {self.player.health} HP | ENEMY: {self.enemy.health} HP")
        print("-" * 30)
        for log in self.logs[-5:]: # Show last 5 lines
            print(log)

    def start_battle(self):
        self.spawn_enemy()
        self.is_fighting = True
        
        # This is the "Real-Time" Loop
        while self.is_fighting:
            self.tickbase.update(self.combat_tick)
            self.render()
            time.sleep(0.05) # Prevent CPU melting
        
        print("\nBattle Over!")

    def character_menu(self):
        print("1. Akira\n2. Simon")
        choice = input("Select: ")
        if choice == "1":
            # Unpacking dictionary and adding a name
            self.player = Entity("Akira", **characters["akira"])
        
        self.start_battle()

if __name__ == "__main__":
    game = Game()
    game.character_menu()