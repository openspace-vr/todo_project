import os
import time

now  = time.strftime("%m/%d/%Y %I:%M:%S %p")
print("It is ", now)

from modules import functions

while True:
    user_action = input("Would you like to display, add, edit, remove or exit? ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
    #if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]#list slicing-slicing 4 characters from the user input


        if os.path.exists(functions.dynamic_path):
         #This will automatically close the file
            todos=functions.get_todos()
            
            todos.append(todo + '\n') #this is a placeholder 

            functions.write_todos(todos)


            # with open(dynamic_path, 'w') as file:
            #     file.writelines(todos)  #This will automatically close the file

           
                
                
            '''   
            file = open(dynamic_path, 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo) #this is a placeholder 

            file = open(dynamic_path, 'w')
            file.writelines(todos)
            file.close()   
            '''


        else:
            '''
            file = open(dynamic_path, 'w')#this happens once. 
            file.writelines(todo)
            file.close()#if this is not here the file will be left open
            '''   
            functions.write_todos(todo + '\n')

    elif user_action.startswith('show'):
        
        try:
            #elif 'show'|'display' in user_action: # | is bitwise or
            todos=functions.get_todos()

            for index, item in enumerate(todos):
                item = item.title()
                item = item.strip("\n")
                row = f"{index+1}-{item}"
                print(row) #This creates break lines
            print("The list length is ", len(todos))
            print(todos) # this will bring an address of the tuple
            list(todos)  # this will print the tuple list
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('edit'):
        try:
            #elif 'edit' in user_action:
            number = int(user_action[5:])
            number -= 1
            #edit_todo = todos[number]
            #print(number, ":", edit_todo)
            todos = functions.get_todos()

            new_todo = input("Please enter new todo: ")
            todos[number] = new_todo + '\n'
            
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
    #elif 'complete' in user_action:
        try:
            number = int(user_action[9:])
            todos=functions.get_todos()

            number -= 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
        except IndexError:
            number = int(user_action[9:])
            print( f"{number} is out of range")
            continue
        
    elif user_action.startswith('exit'):
    #elif 'exit' in user_action:
            break
    
    else: #You should use _ instead of a variable
            print("Unknown command")
        
print("Goodbye")

