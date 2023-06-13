# THIS MODULE IS FOR REGISTERING
import time

# Importing the required libraries / modules here
import checkDatabase
import checkDetails
import sqlite3 as sql

# Register the Roulette App
def registerRouletteApp():

    # Classical page message
    print("\n{:~^30}".format(' REGISTER PAGE '))

    # Users List
    users = []

    # Call checkDatabase Module, get all data in users List
    checkDatabase.checkUsersInDatabase(users)

    # Get user's name and surname
    userNameSurname = input('Enter your name & surname: ')

    while True:
        # Get user's username
        userUsername = input('Enter your username: ').lower()

        # Loop through the user list
        for user in users:
            # If username exists
            if userUsername == user[2]:
                print('This username exists, try another one!\n')
                break
        else:
            print("Username available..")
            break

    # Get user's password
    while True:
        userPassword1 = input('Enter your password: ')          # First password
        userPassword2 = input('Enter your password again: ')    # Second password for auth

        # If passwords don't match
        if userPassword1 != userPassword2 or userPassword2 != userPassword1:
            print('Passwords do not match!\n'
                  'Try again!\n')
            continue

        else:
            break

    print('\n')
    print(f'Your Name & Surname = {userNameSurname},\n'
          f'Your Username = {userUsername},\n'
          f'Your Password = {userPassword2}\n')

    # -> DATABASE CONNECTION STARTS <-

    args = (userNameSurname, userUsername, userPassword1, 100)

    db = sql.connect('mst.sqlite')          # Create connection
    cursor = db.cursor()                    # Create cursor
    command = """
                INSERT INTO
                    users (
                        nameSurname,
                        username,
                        password,
                        money
                           )
                    VALUES (
                        ?, ?, ?, ?
                            )
              """
    cursor.execute(command, args)           # Execute command with args
    db.commit()                             # Commit changes
    db.close()                              # Close connection

    # -> DATABASE CONNECTION ENDS <-

    # Redirect user to login page and let the game start itself
    print('Redirecting to login page in..')
    time.sleep(1.5)
    print(3)
    time.sleep(1.5)
    print(2)
    time.sleep(1.5)
    print(1)
    time.sleep(2)
    checkDetails.logInRouletteApp()
