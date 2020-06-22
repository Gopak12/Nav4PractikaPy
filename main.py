from file_editor import FileEditor
from read_from_file import ReadFromFile
from program import Program


def main():
    INSTRUCTION = """
0 - exit
1 - sort by name in non-decreasing order
2 - sort by name in non-increasing order
3 - sort by destination in non-decreasing order
4 - sort by destination in non-increasing order
5 - sort by flight number in non-decreasing order
6 - sort by flight number in non-increasing order
7 - sort by price in non-decreasing order
8 - sort by price in non-increasing order
9 - find aeroflots with provided destination
10 - find aeroflots with provided name
11 - find aeroflots with provided departure day
12 - add new aeroflot
13 - delete aeroflot by index
14 - edit aeroflot(enter index and field which you want to change)
15 - print aeroflots
"""
    print(INSTRUCTION)
    path_read = input("enter path_read: ")
    path_write = input("enter path_write: ")
    reader = ReadFromFile(path_read)
    file = FileEditor(path_write)


    collection = reader.read()
    menu = Program(collection)
    while True:
        try:
            menu.menu(file)
        except Exception as s:
            print(s)

if __name__ == '__main__':
    main()
