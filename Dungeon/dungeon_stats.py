##This class contains the various stats to be used in the game, including both Player and Enemy stats.


def stats():
    print "HP:   ", health, "/", max_health
    print "MP:   ", mana, "/", max_mana
    print "ATK:  ", attack
    print "DEF:  ", defense
    print "M-ATK:", magic_attack
    print "EXP:  ", exp


level = 1
max_health = 100
health = 100
max_mana = 20
mana = 20
exp = 0
attack = 1
defense = 1
magic_attack = 2
random_battle = 0
escape = 0

#Enemies
enemy_hp = 0
enemy_attack = 0
enemy_defense = 0
enemy_exp = 0