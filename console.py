#!/usr/bin/python3
"""
main entry point for console tool
"""


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    this is the main entry point
    for the airbnb console tool
    """
    prompt = "(hbnb) "
    # intro = "Welcome to Ella's Airbnb :)"

    def do_EOF(self, line):
        """
        to implement end of file, ctrl d
        """
        return True

    def do_quit(self, line):
        """
        to implement quitting the program
        """
        return True

    def emptyline(self):
        """
        to handle empty lines
        """
        pass

    def help_quit(self):
        """
        help about quit function
        """
        print("wanna quit?")
    
    def do_create(self, command):
        """
        creates a new instance of BaseModel
        saves it to json file
        prints the id
        """
        if not command:
            print("*** class name missing ***")
            return None
        command = command.split()
        if command[0] == "BaseModel":
            newBaseModel = BaseModel()
            newBaseModel.save()
            print(newBaseModel.id)
        else:
            print("*** class doesn't exist ***")


if __name__ == '__main__':
    HBNBCommand().cmdloop()