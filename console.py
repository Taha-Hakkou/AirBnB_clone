#!/usr/bin/env python3
"""
HBnB Console
"""
import cmd, sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.engine.file_storage import FileStorage


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
        'create'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        else:
            obj = cls[args[0]]()
            obj.save()
            print(f"{obj.id}")

    def do_show(self, arg):
        'show'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in FileStorage.__objects.keys():
            print("** no instance found **")
        else:
            print(FileStorage.__objects[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        'destroy'
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif clsname not in cls.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in FileStorage.__objects.keys():
            print("** no instance found **")
        else:
            FileStorage.__objects.pop(f"{args[0]}.{args[1]}")

    def do_all(self, arg):
        'all'
        args = arg.split()
        if len(args) == 0:
            for obj in FileStorage.__objects.values():
                print(obj)
        elif args[0] not in cls.keys():
            print("** class doesn't exist **")
        else:
            for obj in FileStorage.__objects.values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)

    def do_update(self, arg):
        'update'
        args = arg.split()
        clsname, id, attr, value = args[0], args[1], args[2], args[3]
        if len(args) == 0:
            print("** class name missing **")
        elif clsname not in cls.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in FileStorage.__objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = FileStorage.__objects[f"{args[0]}.{args[1]}"]
            setattr(obj, args[2], type(getattr(obj, args[2]))(value))
            obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
