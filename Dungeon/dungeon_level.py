import dungeon_stats

def level_check():
    if dungeon_stats.level == 1:
        if dungeon_stats.exp >= 200:
            print "Congratulations! You have reach level 2!"
            dungeon_stats.max_health += 50
            dungeon_stats.health = dungeon_stats.max_health
            dungeon_stats.max_mana += 10
            dungeon_stats.mana = dungeon_stats.max_mana
            dungeon_stats.attack += 1
            dungeon_stats.defense += 1
            dungeon_stats.magic_attack += 1
            dungeon_stats.level = 2
            print """            Max HP increased by 50
            Max Mana increased by 10
            Attack increased by 1
            Defense increased by 1
            Magic Attack increased by 1"""
        else:
            print "You are", (200 - dungeon_stats.exp), "Away from level 2"
    elif dungeon_stats.level == 2:
        if dungeon_stats.exp >= 1000:
            print "Congratulations! You have reach level 3!"
            dungeon_stats.max_health += 70
            dungeon_stats.health = dungeon_stats.max_health
            dungeon_stats.max_mana += 15
            dungeon_stats.mana = dungeon_stats.max_mana
            dungeon_stats.attack += 4
            dungeon_stats.defense += 3
            dungeon_stats.magic_attack += 4
            dungeon_stats.level = 3
            print """            Max HP increased by 70
            Max Mana increased by 15
            Attack increased by 4
            Defense increased by 3
            Magic Attack increased by 4"""
        else:
            print "You are", (1000 - dungeon_stats.exp), "Away from level 3"
    elif dungeon_stats.level == 3:
        if dungeon_stats.exp >= 4000:
            print "Congratulations! You have reach level 4!"
            dungeon_stats.max_health += 80
            dungeon_stats.health = dungeon_stats.max_health
            dungeon_stats.max_mana += 25
            dungeon_stats.mana = dungeon_stats.max_mana
            dungeon_stats.attack += 8
            dungeon_stats.defense += 5
            dungeon_stats.magic_attack += 8
            dungeon_stats.level = 4
            print """            Max HP increased by 80
            Max Mana increased by 25
            Attack increased by 8
            Defense increased by 5
            Magic Attack increased by 8"""
        else:
            print "You are", (4000 - dungeon_stats.exp), "Away from level 4"
    elif dungeon_stats.level == 4:
        if dungeon_stats.exp >= 10000:
            print "Congratulations! You have reach level 5!"
            dungeon_stats.max_health += 90
            dungeon_stats.health = dungeon_stats.max_health
            dungeon_stats.max_mana += 10
            dungeon_stats.mana = dungeon_stats.max_mana
            dungeon_stats.attack += 5
            dungeon_stats.defense += 9
            dungeon_stats.magic_attack += 3
            dungeon_stats.level = 5
            print """            Max HP increased by 90
            Max Mana increased by 10
            Attack increased by 5
            Defense increased by 9
            Magic Attack increased by 3"""
        else:
            print "You are", (10000 - dungeon_stats.exp), "Away from level 5"
    elif dungeon_stats.level == 5:
        if dungeon_stats.exp >= 18000:
            print "Congratulations! You have reach level 5!"
            dungeon_stats.max_health += 100
            dungeon_stats.health = dungeon_stats.max_health
            dungeon_stats.max_mana += 0
            dungeon_stats.mana = dungeon_stats.max_mana
            dungeon_stats.attack += 8
            dungeon_stats.defense += 2
            dungeon_stats.magic_attack += 2
            dungeon_stats.level = 5
            print """            Max HP increased by 100
            Max Mana increased by 0
            Attack increased by 8
            Defense increased by 2
            Magic Attack increased by 2"""
        else:
            print "You are", (18000 - dungeon_stats.exp), "Away from level 5"
    else:
        print "Probable Error...Review dungeon_level"