 # INF360 Programming in Python
# Catherine Schnelle
# Final Project

#import modules
import time
import sys
import pygame


# inventory list - starts empty
inv = []


# start lvl
# player starts here after main menu
def start():
    print('\nYou find yourself standing at the edge of a beach.')
    time.sleep(1)
    choice = input('What would you like to do? => ')  # user prompt for input
    if choice == "look":     # description
        print("\nIt is gloomy and cold. You shiver.")
        time.sleep(1)
        print('\nYour head is pounding, it feels....empty.')
        time.sleep(1)
        print('\nYou see a lighthouse to your left, a cabin in front of you, and a boat to your right.')
        start()
    elif choice == "forward":
        print('\nYou see a cabin ahead. It is weathered and old.')
        choice = input('Would you like to go inside? => ')
        if choice == "yes":
            print('\nYou enter the cabin. The door was wide open. You stand, engulfed in darkness.')
            cabin()           # to cabin lvl
        else:
            start()           # restart lvl
    elif choice == "back":    # movement cmd calls abyss func
        abyss()
    elif choice == "right":   # movement cmd calls crate func after yes input
        print("\nYou see a wrecked boat lying upon the shore.")
        print("There is a crate lying upon the sand next to it.")
        choice = input('Would you like to open the crate? => ')
        if choice == "yes":   # to crate lvl
            crate()
        else:
            start()           # restart lvl
    elif choice == "left":    # to beach 2 lvl
        print('\nYou walk along the beach. The wind rages against your face.')
        beach2()
    elif choice == "inv":     # displays inventory
        print('\nInventory:')
        print(inv)
        start()
    elif choice == "x":       # quits game
        x()
    elif choice == "hint":    # hint
        print("\nUse 'forward', 'right', 'left', and 'back' to explore.")
        print("Use 'look' for insight about your surroundings.")
        start()
    else:                     # invalid cmd
        print("\nYou can't do that here. Type 'hint' if you are stuck.")
        start()
    return


# lighthouse lvl
def lighthouse():
    choice = input('What would you like to do? => ')
    if choice == "look":        # description
        print("\nYou see a spiral staircase before you, a desk to your left, and\na wooden cross lying against the stairs.")
        lighthouse()
    elif choice == "forward":   # level in progress
        print("\nYou climb the staircase to the top.")
        topLighthouse()
    elif choice == "back":      # back to beach2
        print("\nYou walk back along the beach.")
        beach2()
    elif choice == "left":     # walk to desk
        print("\nYou walk over to the desk a see journal with an entry.")
        choice = input("Would you like to read it? => ")
        if choice == "yes":
            print('\n-----------------------------------------------')
            print("I've discovered something that will save us.")
            print("\nHave I gone mad? I know what I saw down there.")
            print("\nI'm not afraid anymore. Our fate is inevitable.")
            print("\n -August")
            print('-------------------------------------------------')
            lighthouse()
        else:
            lighthouse()
    elif choice == "right":     # invalid dir
        print("\nYou can't go that way.")
        lighthouse()
    elif choice == "inv":       # displays inventory
        print('\nInventory:')
        print(inv)
        lighthouse()
    elif choice == "x":          # to quit game
        x()
    elif choice == "hint":       # hint
        print("\nType 'look' for insight about your surroundings.")
        lighthouse()
    else:                       # invalid cmd
        print("\nYou can't do that here. Type 'hint if you are stuck.")
        lighthouse()
    return

# lighthouse top lvl
def topLighthouse():
    choice = input("What would you like to do? => ")
    if choice == "forward":
        print("\nYou lean out of the broken window.")
        time.sleep(1)
        print("\nYou see a body lying on the ground.")
        time.sleep(1)
        print("\nYou remember what happened....")
        time.sleep(1)
        print("\nYou discover your true nature.")
        gameOver()             # game over
    elif choice == "back":     # back to lighthouse lvl
        print("\nYou climb down the stairs.")
        lighthouse()
    elif choice == "look":  # lvl description
        while "key" in inv:
            print("\nYou already have the key.")
            topLighthouse()
        else:
            print("\nYou see the window in front of you has been shattered.")
            print("\nHanging above it is a key attached to a string.")
            choice = input("Do you want to take it? => ")
            if choice == "yes":
                inv.append("key")  # adds key to inv
                print("\nYou grab the key and place it into your pocket.")
                time.sleep(1)
                print("\nThere's nothing left to find here.\nYou walk back down the stairs.")
                lighthouse()  # back to lighthouse lvl
            else:
                print("You leave the key.")
                topLighthouse()
    elif choice == "inv":       # displays inventory
        print('\nInventory:')
        print(inv)
        topLighthouse()
    elif choice == "x":          # to quit game
        x()
    elif choice == "hint":      # hint
        print("\nType 'look' for insight about your surroundings.\n Type 'forward', 'back', 'right' and 'left' to move.")
        topLighthouse()
    elif choice == "right" or "left":   # invalid dir
        print("You can't go that way.")
        topLighthouse()
    else:                       # invalid cmd
        print("\nYou can't do that here. Type 'hint' if you are stuck.")
        topLighthouse()
    return


# cabin lvl
def cabin():
    while "flashlight" in inv:  # options if flashlight in inv
        choice = input('What would you like to do =>')   # user prompt
        if choice == "use flashlight":     # description
            print('\nYou shine your flashlight into the cabin and see a table.')
            print("There is a journal on the table with an entry.")
            time.sleep(1)
            choice = input('\nWould you like to read it? => ')
            if choice == "yes":
                print("\n-----------------------------")
                print("\nThere is no more food or water.")
                print("\nNo one came for us.")
                print("\nI can't bare this much longer.")
                print("\nI can't find the body.")
                print("\n-----------------------------")
                time.sleep(3)
                print('\nThere is nothing left to do here. You must go back.')
                time.sleep(1)
                start()        # lvl completed
            else:
                print("You leave the note behind and walk back outside.")
                start()        # back to start lvl
        elif choice == "back":
            print("\nYou walk back outside.")
            start()
        elif choice == "look":   # lvl description
            print("\nIt is dark. You cannot see.")
            cabin()
        elif choice == "hint":    # hint
            print("\nType 'inv' to check your pockets. Type 'use' followed by the item name.")
            cabin()
        elif choice == "inv":     # displays inv
            print("\nInventory: ")
            print(inv)
            cabin()
        elif choice == "x":       # quit game
            x()
        elif choice == "forward" or "right" or "left":     # invalid dir
            print("\nYou can't walk that way here.")
            cabin()
        else:                  # invalid cmd
            print("\nYou can't do that here. Type 'hint' if you are stuck.")
            cabin()
    else:                      # if flashlight is not in inv
        choice = input('\nIt is too dark. You cannot see.\nDo you want to go back? => ')
        if choice == "yes":
            print("\nYou walk back outside.")
            start()
        else:                  # game over
            print('\nYou stay in the dark cabin.\nYour spirit becomes too attached to leave, \nhaunting it forever.')
            gameOver()
    return


# crate lvl
def crate():
    while "flashlight" in inv:
        print("The crate is empty.")
        start()      # returns to start if player already retrieved flashlight
    else:
        print('The crate is locked.')
        choice = input('Enter the password: => ')    # password puzzle
        if choice == "August":     # correct password
            print('The crate is unlocked.')
            choice = input("\nYou see a flashlight. Do you want to take it? => ")
            if choice == "yes":    # adds flashlight to inv list
                inv.append("flashlight")
                print('\nYou have picked up a flashlight.')
                time.sleep(1)
                print('\nThere is nothing left to do here. You must go back.')
                time.sleep(1)
                start()
            else:                  # does not add to inv
                print('\nYou leave the flashlight in the crate')
                time.sleep(1)
                start()
        else:                      # wrong password
            print('Wrong password.')
            print('Hint: Explore the areas and read notes you may find. The password is case sensitive.')
            choice = input('Do you want to try again? => ')
            if choice == "yes":
                crate()
            else:                  # returns to room 0
                start()
        return


# abyss lvl - game over
def abyss():
    print('\nYou see a vast ocean sprawling for miles with nothing in sight.')
    time.sleep(1)
    print('\nYou walk into it, waves crashing onto you.')
    time.sleep(1)
    print('\nThe abyss takes you.')
    time.sleep(1)
    print('^^^^^^^^^^^^^^^^^^^^')
    gameOver()                  # to game over screen
    return


# beach 2 lvl
def beach2():
    choice = input('What would you like to do? => ')
    if choice == "look":         # lvl description
        print('\nYou see a lighthouse ahead of you.')
        print('To your right along the side of the cabin, shrubs wave back and forth in the sand.')
        beach2()
    elif choice == "forward":    # to lighthouse lvl
        choice = input('\nWould you like to enter the lighthouse? => ')
        if choice == "yes":
            print('\nYou push the door open, heavy with white paint that has been chipping away.')
            print('You enter the lighthouse.')
            lighthouse()
        else:
            beach2()             # restarts lvl
    elif choice == "back":       # returns to room0
        print('\nYou walk back towards a boat along the beach.')
        start()
    elif choice == "right":      # to cabin side lvl
        print('\nYou walk towards the side of the cabin.')
        cabinSide()
    elif choice == "left":       # to abyss lvl (game over)
        abyss()
    elif choice == "inv":        # displays inv
        print('\nInventory:')
        print(inv)
        beach2()
    elif choice == "x":          # quits game
        x()
    elif choice == "hint":        # hint
        print("\nTry 'look' for insight about your surroundings. Try 'forward', 'back', 'right', and 'left' to move.")
        beach2()
    else:                        # invalid cmd
        print("\nYou can't do that here. Type 'hint' if you are stuck.")
        beach2()
    return


# cabinSide lvl
def cabinSide():
    choice = input('What would you like to do? => ')
    if choice == "look":        # lvl description
        print('\nYou see an empty field in front of you.')
        cabinSide()
    elif choice == "back":      # back to beach2 lvl
        print('\nYou walk back towards the beach.')
        beach2()
    elif choice == "forward":   # to field lvl
        print("\nYou find yourself in a field.")
        field()
    elif choice == "inv":       # displays inv
        print('\nInventory:')
        print(inv)
        cabinSide()
    elif choice == "x":         # quits game
        x()
    elif choice == "hint":      # hint
        print("\nType 'look' for insight about your surroundings. Try 'forward', 'back', 'right', and 'left' to move.")
        cabinSide()
    elif choice == "right" or "left":
        print("You can't go that way.")
        cabinSide()
    else:                      # invalid cmd
        print("\nYou can't do that here. Type 'hint' if you are stuck.")
        cabinSide()
    return


# field lvl
def field():
    choice = input('What would you like to do? => ')
    if choice == "look":        # lvl description
        print('\nYou see a grate on the ground in front of you.')
        print("While the familiar still lies behind you, there is nothing else in sight.")
        field()
    elif choice == "forward":   # to grate level(unfinished)
        print("\nYou approach the grate.")
        grate()
    elif choice == "back":      # back to cabin side lvl
        print("\nYou walk back to the side of the cabin.")
        cabinSide()
    elif choice == "hint":
        print("\nType 'look' for insight about your surroundings.")
        field()
    elif choice == "inv":       # displays inv
        print('\nInventory:')
        print(inv)
        field()
    elif choice == "x":          # quits game
        x()
    elif choice == "right" or "left":   # invalid dir
        print("\nYou can't go that way.")
        field()
    else:                        # invalid cmd
        print("\nYou can't do that here. Type 'hint' if you are stuck.")
        field()
    return


# grate lvl
def grate():
    while "key" in inv:
        choice = input("What do you want to do? => ")
        if choice == "look":                    # lvl description
            print("\nYou see there is a latch with a lock.")
        elif choice == "use key":               # use item key if in inv - to bunker lvl
            print("\nYou unlock the grate, exposing a ladder.\nYou climb down.")
            bunker()
        elif choice == "back":                  # back to field lvl
            print("\nYou walk back to the field.")
            field()
        elif choice == "inv":                   # displays inv
            print('\nInventory:')
            print(inv)
            grate()
        elif choice == "x":                     # quits game
            x()
        elif choice == "hint":
            print("\nYou'll need to unlock the grate with your key. Try 'use' followed by the item name.")
            grate()
        elif choice == "right" or "left" or "forward":  # invalid dir
            print("\nYou can't go that way.")
            grate()
        else:                                   # invalid cmd
            print("\nYou can't do that here. Type 'hint' if you are stuck.")
            grate()
    else:
        choice = input("What do you want to do? => ")
        if choice == "look":                    # lvl description
            print("\nYou see there is a latch with a lock that requires a key.")
            print("\nYou need to go back and find it.")
            time.sleep(1)
            print("\nYou walk back to the field.")
            field()
        elif choice == "forward" or "right" or "left":  # invalid dir
            print("\nYou can't go that way.")
            grate()
        elif choice == "back":                  # back to field lvl
            print("\nYou walk back to the field.")
            field()
        elif choice == "inv":                   # displays inv
            print("\nInventory: ")
            print(inv)
            grate()
        elif choice == "x":                     # quits game
            x()
        elif choice == "hint":                  # hint
            print("\nYou'll need to go back and find a key. Try 'inv' to check your pockets.")
            grate()
        else:
            print("\nYou can't do that here. Type 'hint' if you are stuck.")   # invalid cmd
            grate()
    return


# bunker lvl
def bunker():
    while "flashlight" in inv:
        choice = input("What do you want to do? => ")
        if choice == "forward":             # game over lvl
            print("\nYou walk forward into the darkness.")
            time.sleep(1)
            print('\nThe abyss takes you.')
            time.sleep(1)
            print('^^^^^^^^^^^^^^^^^^^^')
            gameOver()
        elif choice == "look":              # lvl description
            print("\nBefore you lies complete and total darkness.")
            bunker()
        elif choice == "inv":               # displays inv
            print("\nInventory: ")
            print(inv)
            bunker()
        elif choice == "use flashlight":    # use flashlight if in inv
            print("\nYou turn on your flashlight.")
            choice = input("\nYou see a metal door a few steps ahead. Do you choose to move forward? => ")
            if choice == "yes":              # to tunnel lvl
                print("\nYou walk a few steps forward towards a metal door. There's something on it.")
                tunnel()
            else:
                print("\nYou stay where you are.")    # restart bunker lvl
                bunker()
        elif choice == "back":              # back to grate lvl
            print("\nYou climb up the ladder.")
            grate()
        elif choice == "hint":              # hint
            print("\nSomething in your pockets may help to you see. Type 'use' followed by an item name.")
            bunker()
        elif choice == "x":                 # quits game
            x()
        elif choice == "right" or "left":   # invalid dir
            print("\nYou are in a tunnel. You can't go that way.")
            bunker()
        else:                               # invalid cmd
            print("\nYou can't do that here. Type 'hint' if you are stuck.")
            bunker()
    else:
        choice = input("What do you want to do => ")
        if choice == "forward":             # game over lvl
            print("\nYou walk forward into the darkness.")
            time.sleep(1)
            print('\nThe abyss takes you.')
            time.sleep(1)
            print('^^^^^^^^^^^^^^^^^^^^')
            gameOver()
        elif choice == "look":             # lvl description
            print("\nBefore you lies complete and total darkness.")
            bunker()
        elif choice == "inv":              # displays inv
            print("\nInventory: ")
            print(inv)
            bunker()
        elif choice == "x":                # quits game
            x()
        elif choice == "hint":             # hint
            print("\nYou'll need something to help you see. Go back and find something useful.")
            bunker()
        elif choice == "right" or "left":  # invalid dir
            print("\nYou are in a tunnel. You can't go that way.")
            bunker()
        else:                              # invalid cmd
            print("\nYou can't do that here. Type 'hint' if you are stuck.")
            bunker()
    return


# tunnel lvl
def tunnel():
    choice = input("What would you like to do? => ")
    if choice == "look":                       # lvl description
        choice = input("\nYou see a note pinned to a metal door.\nDo you want to read it? => ")
        if choice == "yes":                    # read note
            print("\n-------------------------------------")
            print("If you're reading this,\nit means you have suffered a similar fate.")
            print("I tried to tell you,\nwe could start over again.\nI have found a way.")
            print("Open the door and let it take you.\nThe spirit cannot stay behind.\n")
            print("always, August")
            print("-------------------------------------")
            time.sleep(2)
            choice = input("\nDo you want to open the door? => ")
            if choice == "yes":                 # open door
                print("\nYou push open the door with all of your might.")
                time.sleep(1)
                print('\nIt bursts open.')
                time.sleep(2)
                print("\nBefore you is total darkness. Your flashlight is useless here.")
                choice = input("\nDo you want to walk through? => ")
                if choice == "yes":         # to oblivion lvl
                    print("\nYou step forward into oblivion.")
                    oblivion()
                else:                           # invalid cmd
                    print("\nYou decide to stay behind in the darkness.")
                    time.sleep(1)
                    print("\nYour spirit becomes too attached to leave,\nhaunting it forever.")
                    gameOver()
        else:
            print("You ignore the note.")
            tunnel()
    elif choice == "back":                      # back to bunker lvl
        print("\nYou walk back towards the ladder.")
        bunker()
    elif choice == "x":                         # quits game
        x()
    elif choice == "hint":                      # hint
        print("\nType 'look' for insight about your surroundings.")
        tunnel()
    elif choice == "forward":                   # invalid dir
        print("\nYou try to step forward but something is blocking your way.")
        tunnel()
    elif choice == "right" or "left":           # invalid dir
        print("\nYou are in a tunnel. You can't go that way.")
        tunnel()
    else:
        print("\nYou can't do that here. Type 'hint' if you are stuck.")      # invalid cmd
        tunnel()
    return


# oblivion lvl - win game
def oblivion():
    # 3rd party module
    # stop main loop music
    pygame.mixer.music.stop()
    # initialize mixer
    pygame.mixer.init()
    # load .wav
    pygame.mixer.music.load('Sea_Space.wav')
    # play .wav (on loop until exit program.)
    pygame.mixer.music.play()
    time.sleep(2)
    print("\nYou succumb to the weightlessness.")
    time.sleep(2)
    print("\nYou close your eyes and let go.")
    time.sleep(3)
    print("\nYou hear a faint voice calling out to you.")
    time.sleep(3)
    print('\nYou find yourself standing at the edge of a beach...')
    time.sleep(3)
    print("\nYou see August walking towards you. The waves slowly retreating back to sea.")
    time.sleep(3)
    print("\nAugust says,\n'Do you think rescue will arrive soon? We're beginning to run low on supplies.'")
    time.sleep(3)
    print('\n\n')
    time.sleep(1)
    print('**************************************************************************************************\n\n')
    time.sleep(1)
    print(' ####     #   #      ###      ####     #####          ####      #####      ##       ####     #   #')
    time.sleep(1)
    print('#         #   #     #   #    #           #            #   #     #         #  #     #         #   #')
    time.sleep(1)
    print('# ###     #####     #   #    ####        #            #####     ####     ######    #         #####')
    time.sleep(1)
    print('#   #     #   #     #   #        #       #            #   #     #        #    #    #         #   #')
    time.sleep(1)
    print(' ####     #   #      ###     ####        #            ####      #####    #    #     ####     #   #\n\n')
    time.sleep(1)
    print('**************************************************************************************************\n')
    time.sleep(1)
    print('~ ~ ~ ~ ~ ~ ~ ~ ~                  ~ ~ ~ ~ ~                                        ~ ~ ~ ~ ~ ~ ~')
    time.sleep(1)
    print('   ~ ~ ~ ~         ~ ~ ~ ~ ~ ~ ~ ~         ~ ~ ~ ~ ~ ~           ~ ~ ~ ~ ~      ~ ~ ~ ~  ')
    time.sleep(1)
    print('	     ~ ~ ~ ~	    ~ ~ ~ ~ ~ ~             ~ ~ ~ ~ ~ ~ ~         ~ ~ ~ ~ \n\n')
    time.sleep(1)
    print("by: Cat Schnelle")
    time.sleep(1)
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("Thank you for playing Ghost Beach.")
    choice = input("Type 'x' to exit the game. => ")
    if choice == "x":
        sys.exit()  # exits program
    return


# quit screen
def x():
    print('--------------------------------\n\nYou quit too soon. What a shame.\n\n--------------------------------')
    sys.exit()                              # exits program
    return


# game over screen
def gameOver():
    # 3rd party module
    # stop main loop music
    pygame.mixer.music.stop()
    # initialize mixer
    pygame.mixer.init()
    # load .wav
    pygame.mixer.music.load('juno.wav')
    # play .wav (on loop until exit program)
    pygame.mixer.music.play()
    time.sleep(3)
    print('')
    print('********************************************************************\n\n')
    time.sleep(1)
    print(' ####    ##    #       #    ####        ###    #   #    ####    ###')
    time.sleep(1)
    print('#       #  #   ##     ##   #           #   #   #   #   #       #   #')
    time.sleep(1)
    print('# ###   ####   # #   # #   #####       #   #   #   #   ####    ####')
    time.sleep(1)
    print('#   #   #  #   #  # #  #   #           #   #    # #    #       #  #')
    time.sleep(1)
    print(' ####   #  #   #   #   #    ####        ###      #      ####   #   #\n\n')
    time.sleep(1)
    print('********************************************************************\n')
    time.sleep(1)
    print('~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~              ~ ~ ~ ~ ~ ~ ~')
    time.sleep(1)
    print('   ~ ~ ~ ~         ~ ~ ~ ~ ~          ~ ~ ~ ~ ~ ~            ')
    time.sleep(1)
    print('	   ~ ~ ~ ~	          ~ ~ ~ ~ ~                   \n\n')
    time.sleep(2)
    print('\nThank you for playing Ghost Beach.\n')
    time.sleep(1)
    choice = input("Type 'x' to exit game. => ")
    if choice == "x":
        sys.exit()                             # exits program
    return