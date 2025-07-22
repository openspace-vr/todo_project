import FreeSimpleGUI as fsgui

from D16.gui import values

feet_label = fsgui.Text("Enter Feet")
feet_box = fsgui.Input()
#files_button = fsgui.FileBrowse("Select Files")

inches_label = fsgui.Text("Enter Inches")
inches_box = fsgui.Input()
#destination_button = fsgui.FolderBrowse("Destination Folder")

convert_button = fsgui.Button("Convert")

window = fsgui.Window('Compress App', layout=[[feet_label, feet_box],
                                              [inches_label, inches_box],
                                              [convert_button]])

print(event, values)
window.read()
window.close()