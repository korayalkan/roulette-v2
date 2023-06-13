# THIS MODULE IS FOR CHECKING THE DATABASE

# Import required libraries / modules here
import sqlite3 as sql

# The function for checking the database
def checkUsersInDatabase(listName):

    # Create a connection
    db = sql.connect('mst.sqlite')

    # Create a cursor
    cursor = db.cursor()

    # Command for executing
    command = """
                SELECT * FROM users
              """

    # Execute command
    cursor.execute(command)

    # A variable for getting users
    userDatas = cursor.fetchall()

    # Loop through the userDatas
    for data in userDatas:
        listName.append(data)

    # Commit changes
    db.commit()

    # Close connection
    db.close()

    # Return the list
    return listName


# For testing, run the function
