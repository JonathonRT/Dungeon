import random
import dungeon_stats
import dungeon_battle

##This is just a basic intro, and then starts the main part of the game.
def intro():
    print """Welcome to Dungeon, Where you will bettle great monsters, And seek great treasures. Shall we begin?"""
    main()

##The main part of the game, here users decide what to do, like check stats, or initiate a battle.
def main():
    print "What would you like to do?"
    action = raw_input ("> ")
    if action == "stats":
        dungeon_stats.stats()
        main()
    elif action == "help":
        print """Type "stats" to check your current stats, uncluding health, mana, etc. Type "battle" to begin a battle. Type "exit" to quit."""
        main()
    elif action == "exit":
        exit(0)
    elif action == "battle":
        dungeon_battle.battle()
        main()
    else:
        print 'try typing "help" for a list of commands.'
        main()


##These are the basic instructions to greet the player, and start the game.
start = 1
if start == 1:
    start = 0
    intro()