import subprocess
import sys
import FreeSimpleGUI as sg
# from zip_creator import make_archive
import os
from pathlib import Path

def run_program1():
    """compress_file.py."""
    try:
        subprocess.run([sys.executable, 'compress_file.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing File compression program : \n{e}")

def run_program2():
    """Runs extract_file.py."""
    try:
        subprocess.run([sys.executable, 'extract_file.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing File extraction program : \n{e}")

def display_menu():
    """Displays the menu options."""
    print("\n--- Main Menu ---")
    print("1. File compression")
    print("2. File Extraction")
    print("3. Exit")
    print("-----------------")

def main():
    """Main function to handle menu interaction."""
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            run_program1()
        elif choice == '2':
            run_program2()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


sg.theme('DarkAmber') 

MENU_LIST = ["1 - File Compression", "2 - File Extrector", "3 - Exit"]
label1 = sg.Text("Main Menu")

list_box = sg.Listbox(tooltip="Select option and click Choice button",
                      size=(25,4), key='choice', enable_events=True,
                      values=MENU_LIST)
choice_button = sg.Button("Choice", key='choiceBtn')
fc_layout = [[label1],
             [list_box],
             [choice_button]]
# Create the window
window = sg.Window("File compressCompress/Extract utility ", layout=fc_layout)
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case sg.WIN_CLOSED:
            exit(0)
        case 'choiceBtn':
            selection = values['choice'][0]
            if selection == "3 - Exit":
                print("Closing the application !!")
                exit(0)
            elif selection == "1 - File Compression":
                run_program1()
            elif selection == "2 - File Extrector":
                run_program2()
            else:
                pass

    


# close the window
window.close()

# if __name__ == "__main__":
#    main()