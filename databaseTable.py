# importing sql
import sqlite3

# select function to show full contents of a table
# primary key = Username
def Select (cursor, query, args=()):
  cursor.execute(query, args)
  records = cursor.fetchall()
  print("Total rows are:  ", len(records))
  if len(records) > 0:
    for row in records:
        print(row)

try:
    sqlite_create_leaderboard_table_query = """CREATE TABLE `Leaderboard`
                                        ('Username' Text NOT NULL,'Wins' INT NOT NULL, 'Losses' INT NOT NULL, PRIMARY KEY (Username))"""

    sqlite_exists_leaderboard_table_query = """SELECT count(name)
                                FROM sqlite_master
                                WHERE type='table'
                                AND name='Leaderboard'"""

# REPLACE instead of INSERT in case the record already exists
    sqlite_insert_leaderboard_query = """REPLACE INTO `Leaderboard` 
                          ('Username','Wins', 'Losses')
                          VALUES (?, ?, ?)"""

# fill the table with some default values to start if never run before
    recordsToInsertLeaderboard = [('Hanna','1000', '0'), ('Joe','0','1000')]

    sqlite_select_leaderboard_query = """SELECT * from `Leaderboard`"""      

    sqliteConnection = sqlite3.connect('python_db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

# get the count of tables with the name Leaderboard
    cursor.execute(sqlite_exists_leaderboard_table_query)

# if the count is 1, then the table exists
    if not cursor.fetchone()[0]==1:
      cursor.execute(sqlite_create_leaderboard_table_query)
      sqliteConnection.commit()
      ###
      print("SQLite table created")

# load the Leaderboard table with the default data
    cursor.executemany(sqlite_insert_leaderboard_query, recordsToInsertLeaderboard)
    sqliteConnection.commit()
  ###
    print("Total", cursor.rowcount, "Records inserted successfully into Leaderboard table")

  
# close the cursor used for CRUD
    cursor.close()

except sqlite3.Error as error:
    print("Error while running sqllite script", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
#        print("sqlite connection is closed")

# connect and disconnect function from python_db
def get_connection():
    connection = sqlite3.connect('python_db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()