#Only run when first setting up the database

import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()

# with open('schema.sql', 'r') as f:
#     connection.executescript(f.read())

fd = open('schema.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')

# Execute every command from the input file
for command in sqlCommands:
    try:
        cur.execute(command)
    except:
        print("Command skipped: ")


cur.execute("INSERT INTO Volunteers (firstName, lastName, email, phone, whyHelp) VALUES (?, ?, ?, ?, ?)",
            ('Ty','Allembert','tyallembert@gmail.com', '8023807464', 'example text')
            )

cur.execute("INSERT INTO Volunteers (firstName, lastName, email, phone, whyHelp) VALUES (?, ?, ?, ?, ?)",
            ('Nate','Lalor','natelalor@gmail.com', '1234567890', 'example text')
            )

cur.execute("INSERT INTO WebsiteInfo (headerMessage, numMeals) VALUES (?, ?)",
            ('Example Event happening May 10th', '400')
            )

connection.commit()
connection.close()
