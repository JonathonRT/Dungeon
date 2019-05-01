import dungeon_stats
import dungeon_battle


##The main part of the game, here users decide what to do, like check stats, or initiate a battle.
def main():
    print ("What would you like to do?")
    action = input ("> ")
    if action in commands:
        commands[action]()
    elif action == "exit":
        exit(0)
    else:
        print('Type "stats" to check your current stats, uncluding health, mana, etc. Type "battle" to begin a battle. Type "exit" to quit.')





##This is just a basic intro, and then starts the main part of the game.
print('Welcome to Dungeon, Where you will battle great monsters, And seek great treasures. Shall we begin?')
commands = {"stats": dungeon_stats.stats, "battle": dungeon_battle.battle}
while True:
    main()