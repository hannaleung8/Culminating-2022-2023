
# imports sql, the file to create the table, tabulate to create a nice chart, and s system to clear the screen for cleaner user experience
import sqlite3
import databaseTable as h
from tabulate import tabulate
import os


    
# function to search for usernames in database
# prints instructions to user
# asks user what they want to search by and changes select statement based on that
# connects to the database and excecutes query with search criteria
# feches all records to search through
# if user's chosen search is in database, it prints it
# if not, the user will be notified what they searched does not exist
def search_usernames():
  try:
    search_criteria = input("Please input the username you want to search for: ")

    select_query = """SELECT * FROM Leaderboard WHERE Username = ?"""
    connection = h.get_connection()
    cursor = connection.cursor()
    cursor.execute(select_query, (search_criteria,))
    records = cursor.fetchall()
    if(records):
      print("Printing matching Username records: ")
      for row in records:
          print("\n")
          print('Username: ', row[0])
          print("Wins: ", row[1])
          print("Losses: ", row[2])
        
    else:
      print("Sorry, no matching usernames found")
    h.close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print("Error while getting data", error)

    
# function to display all usernames in database
# connects to the database and excecutes query with display criteria
# uses tabulate to create a well formatted table for user 
# error message if inserting data into table does not work
def display_all_usernames():
  try:  
    connection = h.get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Leaderboard"""
    cursor.execute(select_query)
    records = cursor.fetchall()

    table = [("Username", "Wins", "Losses")]
    for row in records:
      table = table + [(row[0], row[1], row[2])]
    print("\n")
    print("\n")
    print(tabulate(table))

  except (Exception, sqlite3.Error) as error:
      print("Error while inserting data", error)

    
# function to add data into Leaderboard table in database
# prints instructions to user
# asks user to input the data they wish to add
# connects to the database and excecutes query with input criteria
# commits to the data to integrate it into the database
# if their username is not the same, it will add it to the database and print a message to the user
# if not, the user will be notified if their data has not been added
def add_username(msg):
  try:
    print("\n")
    input_Username = input(msg)
    input_Wins = 0
    input_Losses = 0
    connection = h.get_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO Leaderboard (Username, Wins, Losses) VALUES (?, ?, ?)"
    insert_data = (input_Username, input_Wins, input_Losses)
    cursor.execute(insert_query, insert_data)
    connection.commit()
    print("Your data has been added. Feel free to use the Display All Usernames action to see your added data in the database or see it by searching it using Search Movies.")
  except (Exception, sqlite3.Error) as error:
      print("Error while inserting data", error)


def database():
# start of the program
  print("Welcome to the Pool Game Database")
  while True:
  
  # action menu
    print("\n")
    print("What would you like to do?")
    print("1. Search Usernames")
    print("2. Display All Usernames")
    print("3. Clear Screen")
    print("4. Return to menu")
    print("5. Add new username")
    action = input ("Enter the number of your Action: ")
  
  # runs action
  # built in error meesage
  # exit command
    if (action == "1"):
      search_usernames()
    elif (action == "2"):
      display_all_usernames()
    elif (action == "3"):
      os.system('clear')
      print ("Your screen has been cleared.")
      print("")
    elif (action == "4"):
      print("\n")
      print("Thank you for using the Movie Database")
      break
    elif (action == "5"):
      add_username("Please enter your username")
      print("\n")

    else:
      print("Please enter the number that goes with the action you want to do")
  