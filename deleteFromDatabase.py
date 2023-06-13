# THIS MODULE IS FOR DELETING VALUES - USERS FROM DATABASE

# Importing required libraries / modules here
import sqlite3 as sql

# Change values in DB
# Currently I am using it to subtract user's money in DB
def subtractValueFromDB(username, money, betAmount):

    # The amount we are going to subtract from users money in DB
    amountForChanging = int(money) - int(betAmount)

    # Arguments here
    args = amountForChanging, username

    # Create a connection
    db = sql.connect('mst.sqlite')

    # Create a cursor
    cursor = db.cursor()

    # The command for changing (UPDATING) the money in DB
    command = f"""
                UPDATE users
                    SET money = ?
                        WHERE username = ?
               """

    # Execute the command
    cursor.execute(command, args)

    # Commit changes
    db.commit()

    # Close connection
    db.close()



# Change value in DB
# Currently I am using it to add amount to user's money in DB
def addToUsersMoneyInDB(money, username):

    # Arguments here
    args = money, username

    # Create a connection
    db = sql.connect('mst.sqlite')

    # Create a cursor
    cursor = db.cursor()

    # The command for changing (UPDATING) the money in DB
    command = f"""
                UPDATE users
                    SET money = ?
                        WHERE username = ?
               """

    # Execute the command
    cursor.execute(command, args)

    # Commit changes
    db.commit()

    # Close connection
    db.close()



# Delete an user from DB
def deleteUserFromDB(usersMoney):

    # Arguments here
    param = usersMoney

    # Create a connection
    db = sql.connect('mst.sqlite')

    # Create a cursor
    cursor = db.cursor()

    # The command for deleting the user in DB
    command = f"""
                DELETE FROM users WHERE money = {usersMoney};
               """

    # Execute the command
    cursor.execute(command)

    # Commit changes
    db.commit()

    # Close connection
    db.close()
