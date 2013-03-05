##This class is used to control the battle system for the game, Including which monster's you run into, as well as the rest of the battle sequence.

import random
import dungeon_stats
import dungeon_level
enemy = 0

##This will start you in a battle depending on what random number it generates.
def battle():
    dungeon_stats.random_battle = random.randint(1,10)
    if dungeon_stats.random_battle >= 1 and dungeon_stats.random_battle <= 5:
        print "A Slime appeared"
        dungeon_stats.enemy_hp = 30
        dungeon_stats.enemy_attack = 2
        dungeon_stats.enemy_defense = 1
        dungeon_stats.enemy_exp = 100
        slime()
    elif dungeon_stats.random_battle >= 6 and dungeon_stats.random_battle <= 10:
        print "A Bat appeared"
        dungeon_stats.enemy_hp = 45
        dungeon_stats.enemy_attack = 3
        dungeon_stats.enemy_defense = 2
        dungeon_stats.enemy_exp = 150
        bat()
    else:
        print "it didn't work..."

##These Definitions control the various commands.
def escape(enemy):
    dungeon_stats.escape = random.randint(1,10)
    if dungeon_stats.escape >= 7:
        print "You have Escaped."
    else:
        print "You failed to escape..."
        enemy()
def help(enemy):
    print """Type "fight" to do a regular attack. Type "magic" to use a magic spell attack. Type "run" if you need to try escaping."""
    enemy()
def fight(enemy):
        dungeon_stats.enemy_hp
        damage = ((random.randint(1,5) * dungeon_stats.attack) / dungeon_stats.enemy_defense)
        dungeon_stats.enemy_hp -= damage
        print "You did ", damage, "damage."
        if dungeon_stats.enemy_hp <= 0:
            print "You won!"
            print "You have gained", dungeon_stats.enemy_exp, "EXP!"
            dungeon_stats.exp += dungeon_stats.enemy_exp
            dungeon_level.level_check()
        else:
            enemy_turn(enemy)
def magic(enemy):
    dungeon_stats.mana
    if dungeon_stats.mana < 5:
        print "You don't have enough Mana..."
        slime()
    else:
        magic_damage = (random.randint(2,15) * dungeon_stats.magic_attack)
        dungeon_stats.enemy_hp -= magic_damage
        print "You cast Magic..."
        print "Slime takes", magic_damage, "In magic damage"
        dungeon_stats.mana -= 5
        if dungeon_stats.enemy_hp <= 0:
            print "You won!"
            print "You have gained", dungeon_stats.enemy_exp, "EXP!"
            dungeon_stats.exp += dungeon_stats.enemy_exp
            dungeon_level.level_check()
        else:
            enemy_turn(enemy)   
def enemy_turn(enemy):
    dungeon_stats.health
    enemy_damage = ((random.randint(1,4) * dungeon_stats.enemy_attack) / dungeon_stats.defense)
    dungeon_stats.health -= enemy_damage
    print "Enemy did ", enemy_damage, "damage to you. You have ", dungeon_stats.health, "remaining."
    if dungeon_stats.health <= 0:
        print "You died!"
        raw_input("> ")
        exit()
    else:
        enemy()
    

##This will initiate a battle against a Slime.
def slime():
    print "What will you do?"
    
    action = raw_input("> ")
    commands[action](slime)

##This will initiate a battle against a Bat.            
def bat():
    print "What will you do?"
    
    action = raw_input("> ")
    commands[action](bat)

    
commands = {"fight": fight, "magic": magic, "run": escape, "help": help}