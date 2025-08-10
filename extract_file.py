import FreeSimpleGUI as sg
from zip_extractor import extract_archive
import os
from pathlib import Path

sg.theme('DarkAmber') 

label1 = sg.Text("Select compressed ZIP file: ")
input1 = sg.Input('',key='input_zip')
choose_source_button =sg.FileBrowse(button_text="Choose", key='srcZip' )

label2 = sg.Text("Select Destination Folder:   ")
input2 = sg.Input('', key='folder_loc')
choose_destination_button =sg.FolderBrowse(tooltip="select folder location to extract from compressed file", 
                                           button_text="Choose", key= 'destBtn')
extract_button = sg.Button("Extract", key='extractBtn')
exit_button = sg.Button("Quit", key='exitBtn')

output_extract_label = sg.Text( key='outputextlbl' , text_color='White')

fe_layout = [[label1 , input1 , choose_source_button],
             [label2, input2, choose_destination_button ],
             [extract_button, exit_button, output_extract_label]]

# Create the window
window = sg.Window("File Extract utility program", layout=fe_layout)
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case sg.WIN_CLOSED | 'exitBtn':
            break
        case 'extractBtn':
            sourcepath = values['srcZip']
            dest_folder = values['destBtn']
            if (sourcepath == '') | (dest_folder == ''):
                ret_val = "You are missing to select zip file or destination folder"
            else:
                # print('sourcepath:', sourcepath)
                # print('dest_folder:' , dest_folder )
                ret_val = extract_archive(sourcepath, dest_folder)
            # ret_val = "Success"
            window['outputextlbl'].update(value=ret_val)

window.close()
