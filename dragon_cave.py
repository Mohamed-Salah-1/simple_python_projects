from email.mime import image
from multiprocessing.connection import wait
import random
import time
from termcolor import colored, cprint

print(''' 		 /\      /\                                               
                /' \.,,,/  \                                               
               /';';..,...,/                                                   
              / /   ,,//,`'`                                                 
             ( ,, '_,  ,,,' ``                                               
             |    /@  ,,, ;" `                                               
            /    .   ,''/' `,``                                              
           /   .     ./, `,, ` ;                                             
        ,./  .   ,-,',` ,,/''\,'                                             
       | O /; ./,,'`,,'' |   |                                               
       |     /   ','    /    |                                               
        \___/'   '     |     |                                               
          `,,'  |      /     `\                                              
               /      |        ~\                                            
	        '       (                                                      
             :                                                               
            ; .         \--                                                  
          :   \         ;''')
time.sleep(3)

# cprint('You are in a land full of dragons. In front of you\n', 'red', attrs=['bold' , 'blink'])

def displayIntro():
    time.sleep(3)
    cprint('\nYou are in a land full of dragons. In front of you\n', 'red', attrs=['bold','blink'])
    time.sleep(3)
    cprint('you see two caves. In one cave, the dragon is friendly\n', 'red', attrs=['bold','blink'])
    time.sleep(3)
    cprint('and will share his treasure with you. The other dragon\n', 'red',attrs=['bold','blink'])
    time.sleep(3)
    cprint('is greedy and hungry, and will eat you on sight.\n', 'red',attrs=['bold','blink'])
    time.sleep(3)
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2 ?)\n')
        cave = input()

    return cave

def checkCave(chosenCave):
    cprint('You approach the cave ... \n' , 'blue' , attrs=['bold' , 'blink'] )
    # time.sleep(2)
    cprint('It is dark and spooky ... \n', 'blue' , attrs=['bold' , 'blink'])
    # time.sleep(2)
    cprint('A larg dragon jumps out in front of you! He opens his jaws and ... \n' , 'blue' , attrs=['bold' , 'blink'])
    # print()
    # time.sleep(4)

    friendlyCave = random.randint(1 , 2)
    if chosenCave == str(friendlyCave):
        cprint('Give you his treasure! 😍 \n' , 'green' , attrs=['bold', 'blink'])
    else:
        time.sleep(3)
        cprint('💀 Gobbles you down in one bite!💀\n' , 'red' , attrs=['bold' , 'blink'])

playAgian = ['yes', 'y']

while playAgian :
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    cprint('\nDo you want to play again? (yes or no)\n' , 'white' , attrs=['bold','blink'] )
    playAgian = input()