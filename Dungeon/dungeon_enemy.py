##This file is a collection of enemies and their stats
import random
import dungeon_stats
import dungeon_battle

##This code generates a random number to select an enemy which will be pushed into the battle code.
def battle_start():
    dungeon_stats.inbattle = 1
    enemy = random.randint(0,1)
    enemies[enemy]()

## SLIME
def enemy_slime():
    dungeon_stats.enemy_name = "Slime"
    dungeon_stats.enemy_hp = 30
    dungeon_stats.enemy_attack = 2
    dungeon_stats.enemy_defense = 1
    dungeon_stats.enemy_exp = 10
    dungeon_stats.escape = 7
    dungeon_stats.item = 'potion'
    dungeon_stats.item_chance = 4
    print ("Slime Appeared!!")

## BAT
def enemy_bat():
    dungeon_stats.enemy_name = "Bat"
    dungeon_stats.enemy_hp = 45
    dungeon_stats.enemy_attack = 3
    dungeon_stats.enemy_defense = 2
    dungeon_stats.enemy_exp = 15
    dungeon_stats.escape = 5
    dungeon_stats.item = 'ether'
    dungeon_stats.item_chance = 2
    print ("Bat Appeared!!")
    
## WOLF
def enemy_wolf():
    dungeon_stats.enemy_name = "Wolf"
    dungeon_stats.enemy_hp = 90
    dungeon_stats.enemy_attack = 5
    dungeon_stats.enemy_defense = 4
    dungeon_stats.enemy_exp = 30
    dungeon_stats.escape = 4
    dungeon_stats.item = 'ether'
    dungeon_stats.item_chance = 3
    print ("Wolf Appeared!!")

enemies = {0:enemy_slime, 1:enemy_bat, 2:enemy_wolf}