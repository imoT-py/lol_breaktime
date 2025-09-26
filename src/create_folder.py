import os
from pathlib import Path

def folder_file():

    directory_path = Path(__file__).resolve().parent.parent
    data_path = directory_path / 'outputs'

    # create outputs folder
    try:
        os.mkdir(data_path)
    except FileExistsError:
        print(f"Directory '{data_path}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{data_path}'.")
    except Exception as e:
        print(f"An error occured: {e}")

    # create users.txt file
    try:
        f = open(str(data_path) + "/" + "users.txt", "x")
        
    except FileExistsError:
            print(f"Directory 'users.txt' already exists.")
    except PermissionError:
            print(f"Permission denied: Unable to create 'users.txt'.")
    except Exception as e:
            print(f"An error occured: {e}")
