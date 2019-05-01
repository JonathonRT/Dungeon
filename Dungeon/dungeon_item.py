import dungeon_stats

inventory = ['potion']

def useitem():
    print('Use which item?', inventory)
    item = input("> ")
    if item in inventory and item in commands:
        commands[item]()
    elif item in inventory:
        print('Cannot use ', item)
        useitem()
    else:
        print(item, 'does not exist!')
        
def potion():
    if dungeon_stats.health == dungeon_stats.max_health:
        print('Health Full!')
    elif dungeon_stats.health >= (dungeon_stats.max_health - 40):
        dungeon_stats.health = dungeon_stats.max_health
        print('Health Restored! ', dungeon_stats.health, "/", dungeon_stats.max_health)
        inventory.remove('potion')
    else:
        dungeon_stats.health += 40
        print('Health Restored! ', dungeon_stats.health, "/", dungeon_stats.max_health)
        inventory.remove('potion')
        
def ether():
    if dungeon_stats.mana == dungeon_stats.max_mana:
        print('Mana Full!')
    elif dungeon_stats.mana >= (dungeon_stats.max_mana - 20):
        dungeon_stats.mana = dungeon_stats.max_mana
        print('Mana Restored! ', dungeon_stats.mana, "/", dungeon_stats.max_mana)
        inventory.remove('ether')
    else:
        dungeon_stats.mana += 20
        print('Mana Restored! ', dungeon_stats.mana, "/", dungeon_stats.max_mana)
        inventory.remove('ether')

commands = {'potion': potion, 'ether': ether}
