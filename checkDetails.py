# THIS MODULE IS FOR LOGGING IN

# Importing the required libraries / modules here
import time
import checkDatabase
import gameRoulette

# Current user's information in DB
currentUser = []


# Log In the Roulette App
def logInRouletteApp():

    # Classical page message
    print("\n{:~^30}".format(' LOGIN PAGE '))

    # User's password, temporary variable
    global tmp

    # Users List
    users = []

    # Call checkDatabase Module, get all data in users List
    checkDatabase.checkUsersInDatabase(users)

    # Get user's username
    userUsername = input('Enter your username: ')

    # Loop through the list named users, find the current user
    # Append it to list named currentUser
    for user in users:
        if user[2] == userUsername:
            currentUser.append(user)
            tmp = user[3]
            break

    # If user does not exist
    else:
        print('This username does not exist!\n'
              'Please restart the program..')
        quit()

    # Get user's password
    i = 3
    while i >= 1:
        userPassword = input('Enter your password: ')

        # If passwords match
        if userPassword == tmp:
            print('Passwords match!\n\n'
                  'Redirecting to the Game...\n')
            time.sleep(1.5)
            gameRoulette.startRouletteApp()
            break

        # If passwords don't match
        elif userPassword != tmp:
            i -= 1
            print(f'Passwords do not match!\n'
                  f'Your lasted tries -> {i}!\n')
            continue



# Get current user
def getCurrentUser():

    return currentUser      # Return the current user



# For testing, run the function here
