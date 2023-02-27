import sqlite3
from tabulate import tabulate
from rich.console import Console
from rich.traceback import install
install()

console = Console(record=True)

def register():
    connection = sqlite3.connect("Userdata.db")
    cur = connection.cursor()

    # Get the previous value of the id field
    cur.execute("SELECT MAX(id) FROM AccountDB")
    previous_id = cur.fetchone()[0]
    if previous_id is None:
        previous_id = 0

    # Prompt user for input
    ID = input(f"Enter user ID (previous userID: {previous_id}): ")
    FirstName = input("Enter first name: ")
    LastName = input("Enter last name: ")
    EMAIL = input("Enter username: ")
    Password = input("Enter password: ")

    # Insert values into database
    cur.execute("INSERT INTO AccountDB (ID,FirstName,LastName,EMAIL,Password) VALUES (?, ?, ?, ?, ?)", (ID,FirstName,LastName,EMAIL,Password ))

    # Display inserted data in tabular format
    cur.execute("SELECT * FROM AccountDB WHERE id = ?", (ID,))
    headers = [description[0] for description in cur.description]
    rows = cur.fetchall()
    print("")
    print(tabulate(rows, headers=headers))
    print("\n New user added!")
    connection.commit()
    connection.close()

register()
# console.save_html("log\\log.html")