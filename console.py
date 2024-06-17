#!/usr/bin/python3
"""
main entry point for console tool
"""


import cmd
import models
from models import storage
import models.base_model


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
            print("** class name missing **")
            return None
        command = command.split()
        if command[0] in models.all_classes:
            newClass = models.all_classes[command[0]]
            initNewClass = newClass()
            initNewClass.save()
            print(initNewClass.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, command):
        """
        prints the string representation of an instance
        based on class name and id
        """
        if not command:
            print("** class name missing **")
            return None
        command = command.split()
        if command[0] in models.all_classes:
            if len(command) == 1:
                print("** instance id missing **")
            else:
                key = command[0] + "." + command[1]
                all_objects = storage.all()
                if key in all_objects:
                    obj = all_objects[key]
                    newClassObject = models.all_classes[command[0]]
                    initNewClassObject = newClassObject(obj)
                    print(initNewClassObject.__str__())
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, command):
        """
        deletes an instance
        based on class name and id
        saves the change in json file
        """
        if not command:
            print("** class name missing **")
            return None
        command = command.split()
        if command[0] in models.all_classes:
            if len(command) == 1:
                print("** instance id missing **")
            else:
                key = command[0] + "." + command[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
