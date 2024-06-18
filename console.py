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
                    initNewClassObject = newClassObject(**obj)
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

    def do_all(self, command):
        """
        prints string representation of all instances
        based or not on class name
        """
        all_objects = storage.all()
        if not command:
            for key, value in all_objects.items():
                className = key.split(".")[0]
                obj = models.all_classes[className]
                newObj = obj(**value)
                print(newObj.__str__())
        else:
            command = command.split()[0]
            if command in models.all_classes:
                for key, value in all_objects.items():
                    className = key.split(".")[0]
                    if command == className:
                        obj = models.all_classes[className]
                        newObj = obj(**value)
                        print(newObj.__str__())
                    else:
                        pass
            else:
                print("** class doesn't exist **")

    def do_update(self, command):
        """
        update an instance based on class name and id
        add or update attribute
        save change to json file
        """
        if not command:
            print("** class name missing **")
        else:
            command = command.split()
            if command[0] not in models.all_classes:
                print("** class doesn't exist **")
            elif len(command) < 2:
                print("** instance id missing **")
                return None
            elif command[0] + "." + command[1] not in storage.all():
                print("** no instance found **")
                return None
            elif len(command) < 3:
                print("** attribute name missing **")
                return None
            elif len(command) < 4:
                print("** value missing **")
                return None
            else:
                keyName = command[0] + "." + command[1]
                className = models.all_classes[command[0]]
                data = storage.all().get(keyName)
                objInstance = className(**data)
                if hasattr(objInstance, command[2]):
                    objType = type(getattr(objInstance, command[2]))
                    setattr(objInstance, command[2], objType(command[3]))
                else:
                    setattr(objInstance, command[2], command[3])
                storage.all()[keyName] = objInstance.to_dict()
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
