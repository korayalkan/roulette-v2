# MAIN FILE (ALL THE TESTINGS ARE GOING TO BE DONE IN HERE)

# Importing required libraries / modules here
import checkDetails
import getDetails
import gameRoulette

# Main Function
def userAction():

    while True:

        try:
            userInput = int(input('1 | Register\n'
                                  '2 | Log In\n'
                                  '3 | Rules     :'))

        except ValueError:
            print('Only numbers allowed!\n')
            continue

        except KeyboardInterrupt:
            print('Keyboard Interrupt got handled!\n')
            continue

        # If Register, redirect
        if userInput == 1:
            getDetails.registerRouletteApp()
            break

        # If Log In, redirect
        elif userInput == 2:
            checkDetails.logInRouletteApp()
            break

        # If Rules, show it
        elif userInput == 3:
            gameRoulette.readRouletteRules()
            continue

        # For quitting
        elif userInput == 9:
            print('Thanks for playing G-Roulette!\n')
            quit()



# For testing, run the function
userAction()
