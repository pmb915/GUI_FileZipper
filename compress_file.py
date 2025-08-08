
import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input(tooltip="use shift/ctrl and select files for multi selection")
choose_source_button =sg.FilesBrowse(button_text="Choose")

label2 = sg.Text("Select Destination Folder:")
input2 = sg.Input(tooltip="select folder location and file name for compressed file")
choose_destination_button =sg.FolderBrowse(button_text="Choose")

exit_button = sg.Button("Quit")

# define the layout
my_layout = [[label1 , input1 , choose_source_button ], [label2, input2, choose_destination_button], [exit_button]]

# Create the window
window = sg.Window("File compress utility program", layout=my_layout)

while True:
    event, values = window.read()
    # if your want to Quit or close Windows
    if (event == sg.WIN_CLOSED)  or event == "Quit":
        break