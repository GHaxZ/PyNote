# created by GHaxZ

# import stuff
import os
import time
from datetime import datetime
import sys


# define stuff
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def intro():
    print(r"  _____       _   _       _        __      ____")
    time.sleep(0.1)
    print(r" |  __ \     | \ | |     | |       \ \    / /_ |")
    time.sleep(0.1)
    print(r" | |__) |   _|  \| | ___ | |_ ___   \ \  / / | |")
    time.sleep(0.1)
    print(r" |  ___/ | | | . ` |/ _ \| __/ _ \   \ \/ /  | |")
    time.sleep(0.1)
    print(r" | |   | |_| | |\  | (_) | ||  __/    \  /   | |")
    time.sleep(0.1)
    print(r" |_|    \__, |_| \_|\___/ \__\___|     \/    |_|")
    time.sleep(0.1)
    print(r"         __/ |                                  ")
    time.sleep(0.1)
    print("        |___/                                    \n\n")


def delete_notes():
    clear()
    for file in os.listdir():
        if file.endswith(".pn"):
            os.remove(file)
    print(" Deleted all notes.\n ", end="")
    time.sleep(1.5)
    clear()


clear()
while True:
    intro()
    time.sleep(0.1)
    print(
        " The commands are: \n\n new = create a new note \n"
        " open = open the program/notes directory \n delete = delete all notes \n"
        " close = close the program\n"
    )
    command = input(" Enter your command: ")
    note = None
    clear()

    if command == "new":
        note = input(" Your Note:\n\n ")
    elif command == "delete":
        while (delete_confirmation :=
                input("\n Are you sure you want to delete all your notes?\n"
                      " (Notes have to be in the same directory to work)\n"
                      "\n 1 = Yes\n 2 = No\n\n ")) not in ["1", "2"]:
            print(f"{delete_confirmation} id not a valid answer.")
            clear()
        if delete_confirmation == "1":
            delete_notes()
    elif command == "close":
        exit(0)
    elif command == "open":
        print(" What notes do you want to open?\n")
        files = [file for file in os.listdir() if file.endswith(".pn")]
        file_num = None
        for index, existing_note in enumerate(files, 1):
            print(f"\t{index} - {existing_note[:-3]}")
            file_num = index
        if file_num is not None:
            while (selected := int(input("\n "))) not in range(1, file_num + 1):
                print(f" {selected} is not a valid file. Please enter again:")
            clear()
            print("\n Press Ctrl-C to exit before End of File.")
            time.sleep(1.5)
            clear()
            with open(files[selected - 1]) as actual_note:
                for line in actual_note.readlines():
                    try:
                        print(line.replace('\n', ''))
                        time.sleep(len(line) * 0.2)
                    except KeyboardInterrupt:
                        break
    else:
        print(f" {command} is not a valid command.\n ", end="")
        time.sleep(1.5)
        continue
    clear()

    if note is not None:
        # save note
        while (save_confirmation := input("\n Do you want to save your note?\n \n 1 = Yes \n 2 = No\n\n ")) \
                not in ["1", "2"]:
            print(f"\n {save_confirmation} is not a valid answer.\n ", end="")
        clear()
        if save_confirmation == "1":
            note_title = input(" Give your note a title: ")
            clear()
            with open(f"{note_title}.pn", "w") as note_vault:
                date_time = datetime.now()
                date_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
                note_vault.write(f"Date: {date_string}\n\n-----{note_title}-----\n\n{note}")
            clear()
            print(" Saved your note in the program directory.\n ", end="")
            time.sleep(2)
            clear()
