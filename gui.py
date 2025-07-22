import os
from modules import functions
import FreeSimpleGUI as fsgui

label = fsgui.Text("Enter a todo")
input_box = fsgui.InputText(tooltip= "Todo", key="Todo")
'''Key is the todo and value entered is the value'''
add_button = fsgui.Button("Add")

list_box = fsgui.Listbox(values=functions.get_todos(), key="Todos",
                         enable_events=True, size=[45, 10])
edit_button = fsgui.Button("Edit")
complete_button = fsgui.Button("Complete")
exit_button = fsgui.Button("Exit")


window = fsgui.Window('Todo App',
                      layout=[[label],
                              [input_box, add_button],
                              [list_box, edit_button, complete_button],
                              [exit_button]],
                      font=('Helvetica 12'))
#if each item is in its own bracket then each item is on it own row


while True:
    event, values = window.read()
    print(1, event)  #The name of the Event
    print(2, values)
    """The todo that is entered and the todo selected """
    #print(3, values['Todos'])
    """The todo selected"""

    match event:
        case 'Add':
            if os.path.exists(functions.dynamic_path):
                todos = functions.get_todos()
                new_todo = values['Todo'] + '\n'
                todos.append(new_todo)
                functions.write_todos(todos)
                window['Todos'].update(values=todos)
            else:
               functions.write_todos(values['Todo'] + '\n')
               window['Todos'].update(values['Todo'])

        case 'Edit':
            edit_todo = values['Todos'][0] #What was selected
            new_todo = values['Todo']

            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo

            functions.write_todos(todos)
            window['Todos'].update(values=todos) #update list values
        case 'Complete':
            edit_todo = values['Todos'][0]
            todos = functions.get_todos()
            todos.remove(edit_todo)
            functions.write_todos(todos) #write list back to the function write_todos
            window['Todos'].update(values=todos)
            window['Todo'].update(value='')# when you are update one value use value otherwise values
        case 'Exit':
            break
        case 'Todos':
            window['Todo'].update(value=values['Todos'][0])
        case fsgui.WIN_CLOSED:
            break

window.close()