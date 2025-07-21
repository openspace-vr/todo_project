import os
from modules import functions
import FreeSimpleGUI as fsgui

label = fsgui.Text("Enter a todo")
input_box = fsgui.InputText(tooltip= "Todo", key="Todo")
'''Key is the todo and value entered is the value'''
add_button = fsgui.Button("Add")

window = fsgui.Window('Todo App',
                      layout=[[label], [input_box, add_button]],
                      font='Helvetica 12')
#if each item is in its own bracket then each item is on it own row


while True:
    event, values = window.read()
    print(event)  #The name of the Event
    print(values) #The key:value pair (Dictionary)
    match event:
        case 'Add':
            if os.path.exists(functions.dynamic_path):
                todos = functions.get_todos()
                new_todo = values['Todo'] + '\n'
                todos.append(new_todo)
                functions.write_todos(todos)
            else:
               functions.write_todos(values['Todo'] + '\n')
        case fsgui.WIN_CLOSED:
            break

window.close()