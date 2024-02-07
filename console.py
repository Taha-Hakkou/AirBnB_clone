#!/usr/bin/env python3
"""
HBnB Console
"""
import cmd
import sys
from datetime import datetime
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage


cls = {'BaseModel': BaseModel, 'User': User,
       'Amenity': Amenity, 'City': City, 'State': State,
       'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        sys.exit()

    def do_EOF(self, arg):
        'EOF (Ctrl+D) to exit the program'
        sys.exit('')

    def emptyline(self):
        'Do nothing'
        pass

    ###########################
    def do_create(self, arg):
        'Creates a new instance of BaseModel'
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        else:
            obj = cls[args[0]]()
            obj.save()
            print(f"{obj.id}")

    def do_show(self, arg):
        'Prints the string representation of an instance'
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        'Deletes an instance'
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            storage.all().pop(f"{args[0]}.{args[1]}")

    def do_all(self, arg):
        'Prints all string representation of all instances'
        args = shlex.split(arg)
        myObjects = []
        if len(args) == 0:
            for obj in storage.all().values():
                myObjects.append(obj.__str__())
            print(myObjects)
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    myObjects.append(obj.__str__())
            print(myObjects)

    def do_update(self, arg):
        'Updates an instance'
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = storage.all()[f"{args[0]}.{args[1]}"]
            try:
                # if instance has that attribute
                otype = type(obj.__dict__[args[2]])
                obj.__dict__[args[2]] = otype(args[3])
            except KeyError:
                obj.__dict__[args[2]] = args[3]
            finally:
                obj.updated_at = datetime.now()
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
