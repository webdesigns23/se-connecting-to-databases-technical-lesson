import sqlite3

conn = sqlite3.connect('data.sqlite')
cur = conn.cursor()

'''Python sqlite3 Interface without pandas'''
# Execute the query
# (This is a special query for finding the table names. You don't need to memorize it.)
# SQLite databases all have a sqlite_master table that stores the schema information

cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")

# Fetch the result and store it in table_names

table_names = cur.fetchall()

table_names

# If we want to get all information about the offices table, we might do something like this (* means all columns):
cur.execute("""SELECT * FROM offices;""")
cur.fetchall()

# Because .execute() returns the cursor object, it is also possible to combine the previous two lines into one line, like so:
cur.execute("""SELECT * FROM offices;""").fetchall()

# Information about the column names can be retrieved from the cursor. Since the most recent query was SELECT * FROM offices; the cursor will contain information about the offices table:
cur.description


import pandas as pd
#If we wanted to combine the previous two steps to make a dataframe with the right column names, that would look like this:
pd.DataFrame(
    data=cur.execute("""SELECT * FROM offices;""").fetchall(),
    columns=[x[0] for x in cur.description]
)

# It is always important to close out any connections when finished
conn.close()






'''Python sqlite3 Interface with pandas: 

This is the most straightforward technique for writing SQL queries within a Python context. We can skip over the use of the cursor via built-in pandas methods.
'''
#Connecting the the Database:
conn = sqlite3.connect("data.sqlite")

#Viewing the list of tables:
df = pd.read_sql("""SELECT name FROM sqlite_master WHERE type = 'table';""", conn)
df

type(df)
pd.core.frame.DataFrame

#Selecting All data from the offices table and viewing the column names from the offices table
pd.read_sql("SELECT * FROM offices;", conn)

#Disconnecting from the Database
conn.close()