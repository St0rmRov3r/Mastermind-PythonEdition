#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randrange

if __name__ == '__main__':
        
    print("""
  __  __           _            __  __ _           _ 
 |  \/  |         | |          |  \/  (_)         | |
 | \  / | __ _ ___| |_ ___ _ __| \  / |_ _ __   __| |
 | |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` |
 | |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| |
 |_|  |_|\__,_|___/\__\___|_|  |_|  |_|_|_| |_|\__,_|

  --  PYTHON EDITION  ------------------------------




Please enter the following settings to start the game
or hit enter to use the default value:

""")

    length = input("- the length of the secret word (default=4) >>> ")
    length = int(length) if (length.isdigit() and int(length)>0) else 4
    
    charset = input("- the set of characters to use (default='0123456789') >>> ")
    charset = charset if charset != "" else "0123456789"

    tries = input("- how many tries the player has (no limit=0, default=10) >>> ")
    tries = int(tries) if (tries.isdigit() and int(length)>=0) else 10

    playagain = True

    while playagain:

        secret = ""
        for i in range(length):
            secret += charset[randrange(len(charset))]

        print("\n\nYou can send 'quit' to quit the game at any time.\nSend 'history' to get a smaller view of all your attempts\n")

        continueGame = True
        history = []
        remaining = tries
        won = False
        print("Legend:\n\tCC = correct char and correct position\n\tWP = correct char but wrong position\n")
        while continueGame:
            attempt = input(">>> ")
            while len(attempt) != length and attempt != "history" and attempt != "quit":
                attempt = input("your attempt must contain "+str(length)+" characters >>> ")

            if attempt == "quit":
                continueGame = False

            elif attempt == "history":
                print("\nLegend:\n\tCC = correct char and correct position\n\tWP = correct char but wrong position\n")
                for i in range(len(history)):
                    print(str(history[i][0])+"  :  "+str(history[i][1])+" CC, "+str(history[i][2])+" WP")

            else:
                cc = 0
                wp = 0
                scr = secret
                intersect = ""

                for i in range(length):
                    if attempt[i] in scr:
                        intersect += attempt[i]
                        scr = scr.replace(attempt[i], "", 1)

                for i in range(length):
                    if attempt[i] == secret[i]:
                        cc += 1

                wp = len(intersect) - cc
                

                history.append([attempt, cc, wp])
                remaining -= 1
                
                print(str(cc)+" CC ; "+str(wp)+" WP")

                if remaining >= 0:
                    print("\nRemaining attempts: "+str(remaining))

                if remaining == 0: continueGame = False
                if cc == 4:
                    continueGame = False
                    won = True

        if won:
            print("\nCongratulations! You guessed the secret word with only "+str(tries-remaining)+" tries!\n\n")

        else:
            print("\nGame over! The secret word was "+str(secret)+"!\n\n")


        playagain = input("Would you like to play again? (y/n) >>> ") in ["y", "Y", "yes", "Yes"]

    input("\n   - Thank you for playing MasterMind - Python Edition!")
    quit()
    
