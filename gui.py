from modules import functions
import FreeSimpleGUI as fsgui

label = fsgui.Text("Enter a todo")
input_box = fsgui.InputText(tooltip= "Todo")
add_button = fsgui.Button("Add")

window = fsgui.Window('Todo App', layout=[[label], [input_box, add_button]])
#if each item is in its own bracket then each item is on it own row
window.read()
window.close()