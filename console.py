#!/usr/bin/python3
"""
main entry point for console tool
"""

import ast
import cmd
import json
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
                    if type(obj) is not dict:
                        print(str(obj))
                    else:
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
                if type(value) is not dict:
                    print(str(value))
                else:
                    obj = models.all_classes[className]
                    newObj = obj(**value)
                    print(newObj.__str__())
        else:
            command = command.split()[0]
            if command in models.all_classes:
                for key, value in all_objects.items():
                    className = key.split(".")[0]
                    if command == className:
                        if type(value) is not dict:
                            print(str(value))
                        else:
                            obj = models.all_classes[className]
                            newObj = obj(**value)
                            print(newObj.__str__())
                    else:
                        pass
            else:
                print("** class doesn't exist **")

    def do_count(self, command):
        """
        retrieve number of instances of a class
        based on class name
        """
        all_objects = storage.all()
        if command:
            command = command.split()[0]
            if command in models.all_classes:
                count = 0
                for key, value in all_objects.items():
                    if command in key:
                        count += 1
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, command):
        """
        update an instance based on class name and id
        add or update attribute
        save change to json file
        """
        if not command:
            print("** class name missing **")
        else:
            if " {" in command:
                newCommandList = []
                command = command.split(" {")
                newCommandList.append(command[0].split()[0])
                newCommandList.append(command[0].split()[1])
                strDict = "{" + command[1]
                print("strdict", strDict)
                if ',' not in strDict:
                    strDict = strDict.replace('" "', '", "')
                if "'" in strDict:
                    strDict = strDict.replace("'", '"')
                fromStrDict = json.loads(strDict)
                newCommandList.append(fromStrDict)
                command = newCommandList
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
                if command[0] + "." + command[1] not in storage.all():
                    print("** no instance found **")
                    return None
                else:
                    if type(command[2]) is dict:
                        keyName1 = command[0] + "." + command[1]
                        className1 = models.all_classes[command[0]]
                        data1 = storage.all().get(keyName1)
                        if type(data1) is dict:
                            objInstance1 = className1(**data1)
                        else:
                            data1 = data1.to_dict()
                            objInstance1 = className1(**data1)
                        for key, value in command[2].items():
                            if hasattr(objInstance1, key):
                                objType1 = type(getattr(objInstance1, key))
                                setattr(objInstance1, key, objType1(value))
                            else:
                                setattr(objInstance1, key, value)
                        storage.all()[keyName1] = objInstance1.to_dict()
                        storage.save()
                    else:
                        print("** value missing **")
                        return None
            else:
                keyName = command[0] + "." + command[1]
                className = models.all_classes[command[0]]
                data = storage.all().get(keyName)
                if type(data) is dict:
                    objInstance = className(**data)
                else:
                    data = data.to_dict()
                    objInstance = className(**data)
                if hasattr(objInstance, command[2]):
                    objType = type(getattr(objInstance, command[2]))
                    setattr(objInstance, command[2], objType(command[3]))
                else:
                    setattr(objInstance, command[2], command[3])
                storage.all()[keyName] = objInstance.to_dict()
                storage.save()

    def default(self, line):
        """
        function to handle unknown commands
        before displaying a custom error message
        doesn't include empty lines
        """
        all_methods = self.all_methods()
        all_classes = models.all_classes
        errorMessage = "** invalid command **"

        try:
            line = line.split(".")
            if len(line) < 2:
                print(errorMessage)
            else:
                formattedCommand = self.parseCommand(line)
                className = formattedCommand["className"]
                methodName = formattedCommand["methodName"]
                methodArguments = formattedCommand["methodArguments"]
                if className in all_classes \
                and methodName in all_methods:
                    method = getattr(self, "do_" + methodName)
                    if callable(method):
                        try:
                            method(" ".join([className, methodArguments]))
                        except:
                            print("something happened")
                    else:
                        print(errorMessage)
                else:
                    print(errorMessage)
        except:
            print(errorMessage)

    def all_methods(self):
        """
        gets list of available methods...
        ...defined in console tool
        """
        all_methods = [method.split("_")[1] \
                       for method in dir(self) \
                        if method.startswith("do_")]
        return all_methods
    
    def parseCommand(self, line):
        """
        parse a line
        return class name, method name, and arguments
        """
        className = line[0]

        parameters = line[1].split("(")
        methodName = parameters[0]

        methodArguments = []
        if len(parameters[1]) > 1:
            arguments = parameters[1][:-1]
            methodArguments = arguments.split(", ")
        methodArguments = " ".join(methodArguments)

        return {
            "className": className,
            "methodName": methodName,
            "methodArguments": methodArguments
        }


if __name__ == '__main__':
    HBNBCommand().cmdloop()
