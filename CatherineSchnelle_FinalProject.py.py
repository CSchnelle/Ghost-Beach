# INF360 Programming in Python
# Catherine Schnelle
# Final Project

#import modules
import sys
import logging
import time
import pygame
from pygame.locals import *


#logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s = %(levelname)s - %(message)s')

try:
    import levels as lev
except:
    logging.critical('Missing levels.py')
    print('Missing levels.py! Program is closing')
    sys.exit()


#main menu
def main():
    #title screen
    print('')
    print(' ####     #   #      ###      ####     #####          ####      #####      ##       ####     #   #')
    print('#         #   #     #   #    #           #            #   #     #         #  #     #         #   #')
    print('# ###     #####     #   #    ####        #            #####     ####     ######    #         #####')
    print('#   #     #   #     #   #        #       #            #   #     #        #    #    #         #   #')
    print(' ####     #   #      ###     ####        #            ####      #####    #    #     ####     #   #\n\n')
    print('**************************************************************************************************\n')
    print('~ ~ ~ ~ ~ ~ ~ ~ ~                  ~ ~ ~ ~ ~                                        ~ ~ ~ ~ ~ ~ ~')
    print('   ~ ~ ~ ~         ~ ~ ~ ~ ~ ~ ~ ~         ~ ~ ~ ~ ~ ~           ~ ~ ~ ~ ~      ~ ~ ~ ~  ')
    print('	     ~ ~ ~ ~	    ~ ~ ~ ~ ~ ~             ~ ~ ~ ~ ~ ~ ~         ~ ~ ~ ~ \n\n')
    print("by: Cat Schnelle")
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
    print("To explore & interact with items in the game, use the following commands:\n")
    print("To move: 'forward', 'left', 'right' and 'back'  To view inventory: 'inv'")
    print("\nTo explore: 'look'  To interact with items: 'use' followed by item name")
    print("\nType 'hint' if you are stuck")
    print("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    #user prompt
    print("Type'go'to start. \nType'x'to exit.")
    #3rd party module
    #initialize pygame mixer
    pygame.mixer.init()
    #load .wav
    pygame.mixer.music.load('Long_Note_One.wav')
    #play .wav (this will play endlessly until it is quit upon game over or oblivion lvl)
    pygame.mixer.music.play()
    #time delay allows for wav file to load
    time.sleep(2)
    choice = input('=> ')
    if choice == "go":      # calls start func - room0
        lev.start()
    elif choice == "x":     # exits game
        sys.exit()
    else:
        print('Invalid command. Try again.')    # invalid cmd
        main()

    return

main()