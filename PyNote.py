#created by GHaxZ

#import stuff
import os
import time
from datetime import datetime
import sys

#define stuff
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def intro():
    print("  _____       _   _       _        __      ____")
    time.sleep(0.1)
    print(" |  __ \     | \ | |     | |       \ \    / /_ |")
    time.sleep(0.1)
    print(" | |__) |   _|  \| | ___ | |_ ___   \ \  / / | |")
    time.sleep(0.1)
    print(" |  ___/ | | | . ` |/ _ \| __/ _ \   \ \/ /  | |")
    time.sleep(0.1)
    print(" | |   | |_| | |\  | (_) | ||  __/    \  /   | |")
    time.sleep(0.1)
    print(" |_|    \__, |_| \_|\___/ \__\___|     \/    |_|")
    time.sleep(0.1)
    print("         __/ |                                  ")
    time.sleep(0.1)
    print("        |___/                                   ")

#command input
while True:
    while True:
        intro()
        time.sleep(0.1)
        print("\n The commands are: \n\n new = create a new note \n open = open the program/notes directory \n delete = delete all notes \n close = close the program")
        command = input("\n Enter your command: ")

        if command == "new":
            break
        elif command == "delete":
            while True:
                clear()
                print("\n Are you sure you want to delete all your notes?\n (Notes have to be in the same directory to work)\n\n 1 = Yes\n 2 = No")
                delete_notes = input("\n ")
                
                if delete_notes == "1":
                    directory = os.listdir()

                    for item in directory:
                        if item.endswith(".txt"):
                            os.remove(item)
                    clear()
                    break
                elif delete_notes == "2":
                    clear()
                    break
                else:
                    print("\n " + delete_notes + " is not a valid answer.")

        elif command == "close":
            sys.exit()

        elif command == "folder":
            path = ""
            os.system(f'start {os.path.realpath(path)}')
            clear()

        else:
            print("\n " + command + " is not a valid command.")
            time.sleep(3)
            clear()

    clear()

    #create note
    title = input("\n Give your note a title: ")

    print("\n Your note: ")
    note = input(" ")

    clear()

    #save note
    while True:
        print("\n Do you want to save your note?\n \n 1 = Yes \n 2 = No")
        save_note = input("\n ")

        if save_note == "1":
            textfile = open(title + ".txt", "w")
            date_time = datetime.now()
            date_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
            textfile.write("Date: " + date_string + "\n \n" + "-----" + title + "-----" + "\n \n" + note)
            textfile.close()
            clear()
            print("\n Saved your note in the program directory.")
            time.sleep(3)
            clear()
            break
        elif save_note == "2":
            clear()
            break
        else:
            print("\n" + " " + save_note + " is not a valid answer.")


