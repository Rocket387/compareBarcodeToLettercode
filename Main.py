#This program has been modified to preserve document information, however this can be easily adapted
#to connect to another database for a scanning project

import pyodbc
import winsound
from os import system
from settings import settings

db_pass = settings.get('PWD')

conn = pyodbc.connect('DRIVER={{SQL Server}};'
                    'SERVER=ENTER SERVER HERE;'
                    'DATABASE=ENTER DATABASE HERER;'
                    'UID=ENTER TABLE HERE;'
                    'PWD={}'.format(db_pass)) #uses password stored in settings.py



def script():
    Series = input("Enter Series:") #asks the user to enter the corresponding series
    Piece = input("Enter Ref:") #asks the user to enter the Ref number

    cursor = conn.cursor()

    #SQL query uses the user input to pull out all info in thedatabase relating to the user input
    cursor.execute("SELECT barcode FROM Table WHERE Series = " + Series + " Ref = " + Piece)
    rows = cursor.fetchall()
    title = [i[0] for i in cursor.description]
    #iterates through the rows
    for row in rows:
        required_number = (row.barcode) #required number equals the barcode number that corresponds to the series + ref number

    user_number = input("Scan a barcode: ") #takes the user input of the barcode being scanned
    print("\n" * 10) #prints the barcode number 10 lines down

    while required_number != user_number: #checks the scan barcode against the series + ref
                                            # if it is not the same the user is asked to keep scanning
        print("No match" + "\n" * 8)
        user_number = input("Try again: ")
        print ("\n" * 15)
    else:
        winsound.Beep(1000, 500)#(frequncy, duration)
        print("MATCH " + user_number) # if the barcode matches the series + ref entered by the user
                                        #the program beeps alerting the user they have found the correct file

    restart = input('Run again? (y/n): ') # asks the user if they would like to start again to scan more files
    if restart == "Y" or restart == "y":
        print("Restarting" + "\n" * 5)
        script()
    if restart == "N" or restart == "n":
        print ("Script terminating. Goodbye.")
script()