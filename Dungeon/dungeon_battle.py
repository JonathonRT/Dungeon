##This class is used to control the battle system for the game, Including which monster's you run into, as well as the rest of the battle sequence.

import random
import dungeon_stats

def battle():
    dungeon_stats.random_battle = random.randint(1,10)
    if dungeon_stats.random_battle >= 1:
        print "A Slime appeared"
        dungeon_stats.slime_hp
        dungeon_stats.slime_hp = 30
        slime()
    else:
        print "it didn't work..."
def slime():
    print "What will you do?"
    
    action = raw_input("> ")
    
    if action == "fight":
        dungeon_stats.slime_hp
        damage = random.randint(3,10)
        dungeon_stats.slime_hp = dungeon_stats.slime_hp - damage
        print "You did ", damage, "damage."
        if dungeon_stats.slime_hp <= 0:
            print "You won!"
            print "You have gained 100 EXP!"
            dungeon_stats.exp = dungeon_stats.exp + 100
        else:
            slime_turn()
    elif action == "magic":
        slime()
    elif action == "run":
        slime()
    else:
        slime()
def slime_turn():
    dungeon_stats.health
    enemy_damage = random.randint(1,10)
    dungeon_stats.health = dungeon_stats.health - enemy_damage
    print "Slime did ", enemy_damage, "damage to you. You have ", dungeon_stats.health, "remaining."
    if dungeon_stats.health <= 0:
        print "You died!"
        raw_input("> ")
        exit()
    else:
        slime()