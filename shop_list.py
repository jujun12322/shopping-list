FILEPATH = "shopping.txt"


def get_items(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_items(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)