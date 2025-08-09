
import FreeSimpleGUI as sg
from zip_creator import make_archive
import os
from pathlib import Path

sg.theme('DarkAmber') 

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input(tooltip="use shift/ctrl and select files for multi selection",key='source')
choose_source_button =sg.FilesBrowse(button_text="Choose", key='srcBtn' , files_delimiter=',')

label2 = sg.Text("Select Destination Folder:")
input2 = sg.Input(tooltip="select folder location and file name for compressed file", key='destination')
choose_destination_button =sg.FolderBrowse(button_text="Choose", key= 'destBtn')

compress_button = sg.Button("Compress", key='compBtn')
exit_button = sg.Button("Quit")

output_label = sg.Text( key='outputlbl' , text_color='White')

# define the layout
my_layout = [[label1 , input1 , choose_source_button ], 
              [label2, input2, choose_destination_button], 
               [compress_button, exit_button, output_label]]

# Create the window
window = sg.Window("File compress utility program", layout=my_layout)

while True:
    event, values = window.read()
    # display text from input1
    
    if event == 'compBtn':
        # print(event)
        # print(values)
        src_list = values['srcBtn'].split(",")
        dest_loc = values['destBtn']
        print("Source list:")
        print(src_list)
        print("Destination Folder:")
        print(dest_loc)
        ret_val = make_archive(src_list, dest_loc )
        window['outputlbl'].update(value=ret_val)
        # print(f"ret_val = {ret_val}")
    # if your want to Quit or close Windows
    if (event == sg.WIN_CLOSED)  or event == "Quit":
        break

window.close()
