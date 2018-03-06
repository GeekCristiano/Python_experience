# Lets' learn how copying file in python

from os import path

def get_info(file_name):
    if path.exists(file_name) and path.isfile(file_name):
        file_path = path.realpath(file_name)

        head, tail = path.split(file_path)
        print("Path to file:", head)
        print("File name:", tail)

get_info("file.txt")
