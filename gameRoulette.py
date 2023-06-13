# THIS IS GAME MODULE

# Importing the required libraries / modules here
import checkDetails
import deleteFromDatabase
import time
import random

# Spin the roulette, get the lucky number
def spinRoulette():

    # Classical page message
    print('=-'*30)
    print(' '*15,'WELCOME TO G-ROULETTE v2 ')
    print('-=' * 30)

    # Winning number between 0-36
    winningNum = random.randint(0, 36)

    # Return the number
    return winningNum



# Roulette rules
def readRouletteRules():

    # Classical page message
    print("\n{:~^86}".format(' RULES PAGE '))
    print('1 -) G-Roulette is pretty easy to play. Just create an account to play if you do not have one.\n'
          '2 -) If you register, you will be redirected to login page. After logging in, you can start playing.\n'
          '3 -) In game, after you bet, we subtract the bet from your money immediately, be careful :)\n'
          '4 -) In close future, you will be able to change your Password, Name Surname and username too!\n'
          'For now, that is all. Have fun...')
    time.sleep(10)
    print('\nReturning to Starting Menu in,')
    time.sleep(1)
    print(3)
    time.sleep(1.5)
    print(2)
    time.sleep(1.5)
    print(1)
    time.sleep(2)
    print('\n')



# Start the game here for users to play
def startRouletteApp():

    # Set all user information global here
    global userId, userNS, userUN, userPW, userMoney, userNum

    # Current user here
    currentUserList = checkDetails.getCurrentUser()

    # Winning number
    winningNumber = spinRoulette()

    # Loop through the currentUserList to get user's money
    for i in currentUserList:
        userId = i[0]
        userNS = i[1]
        userUN = i[2]
        userPW = i[3]
        userMoney = i[4]
        break

    # Numbers that are in black colour
    black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    # Numbers that are in red colour
    red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    # Green colour, only 0 (zero)
    green = 0

    # If user spends all his/her money
    while userMoney == 0:
        deleteFromDatabase.deleteUserFromDB(userMoney)
        print(f'Your balance has just finished,\n'
              f'Your account will be deleted from our Database.\n'
              f'To keep playing, please create new account.\n'
              f'Shutting down the program...')
        time.sleep(2)
        quit()

    while True:
        # Get user's bet as float
        userBet = float(input('Enter your bet amount: '))

        # If bet is higher than user's money
        if userBet > userMoney:
            print('You can not bet more than your balance!\n')
            continue

        # If user tries to bet 0 or less than 0
        elif userBet <= 0:
            print('You can not bet 0 or less than 0!\n')
            continue

        # If user rests (bets all money)
        elif userBet == userMoney:
            print(f'You are about to spend all your money right now,\n'
                  f'Do you want to bet all?  (1/Yes - 2/No)')
            betAreYouSure = int(input(': '))

            # If yes, keep going
            if betAreYouSure == 1:
                # Change user's money from the DB after the bet
                # Because if user loses, app can be restarted and this could be a big bug (money glitch)
                deleteFromDatabase.subtractValueFromDB(userUN, userMoney, userBet)
                break

            # If no, send back to getting bet
            elif betAreYouSure == 2:
                print('\n')
                continue

        # If bet is acceptable, go on
        else:
            # Delete user's money from the DB again after the bet
            deleteFromDatabase.subtractValueFromDB(userUN, userMoney, userBet)
            break

    while True:
        try:
            userNum = int(input('Enter a number to place your bet: '))

        except ValueError:
            print('Only numbers allowed!\n')
            continue

        except KeyboardInterrupt:
            print('Keyboard Interrupt got handled!\n')
            continue

        # If winning number in red
        if userNum == winningNumber and winningNumber in red:
            # Give user 2x of the userBet
            redWon = int(userBet) * 2
            deleteFromDatabase.addToUsersMoneyInDB(redWon, userUN)
            print(f'Congrats!\n'
                  f'Your bet was {userBet},\n'
                  f'You won ${int(redWon)}!\n')
            break

        # If winning number in black
        elif userNum == winningNumber and winningNumber in black:
            # Give user 3x of the userBet
            blackWon = int(userBet) * 3
            deleteFromDatabase.addToUsersMoneyInDB(blackWon, userUN)
            print(f'Congrats!\n'
                  f'Your bet was {userBet},\n'
                  f'You won ${int(blackWon)}!\n')
            break

        # If winning number is green
        elif userNum == winningNumber and winningNumber == green:
            # Give user 20x of the userBet
            greenWon = int(userBet) * 20
            deleteFromDatabase.addToUsersMoneyInDB(greenWon, userUN)
            print(f'Congrats!\n'
                  f'Your bet was {userBet},\n'
                  f'You won ${int(greenWon)}!\n')
            break

        # If user can't guess the winning number
        elif userNum != winningNumber:
            print(f'You could not guess the winning number and lost ${int(userBet)}!\n')
            break

        # Anything else, give an error message and send back to loop
        else:
            print('An error has occurred!\n')
            continue
