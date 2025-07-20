dynamic_path = "todos.txt"
""" 
Functions.py will open the file read the content (get_todos) and
write the data accordingly (write_todos)
"""
print ("Dynamic path defined in functions.py")

""" base_dir = os.path.join("D:","Udemy", "D6")  
sub_dir = "Experiments"
dynamic_path = os.path.join(base_dir, sub_dir,"todos.txt") """


def get_todos():
    with open(dynamic_path, 'r') as file:
        todos_local = file.readlines() #should be a different name that is local
    return todos_local

def write_todos(todos):
    with open(dynamic_path, 'w') as file:
        file.writelines(todos)  #This will automatically close the file

if __name__ == "__main__":
    print("Hello")
    print(get_todos())

    #This will only happen in the functions module
    #__name__ is the name of the function you are currently running (directly). 
    #inside functions is main outside it is the name of the program