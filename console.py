#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

import json

class HBNBCommand(cmd.Cmd):
    """custom cmd for air_bnb"""

    prompt = "(hbnb) "

    model_names = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']
    cmds = ['all', 'show', 'count', 'destroy', 'update']
    def precmd(self, line):
        """Pre command hook"""
        args_arr = line.split('.', maxsplit=1)
        if len(args_arr) == 2:
            model, raw_method = args_arr
            meth_arr = raw_method.split('(', maxsplit=1)
            if len(meth_arr) == 2:
                method, raw_arguments = meth_arr
                arguments = ' '.join(map(lambda x: x.strip(), raw_arguments.rstrip(')').split(',')))
                if model in self.model_names:
                    if method in self.cmds:
                        if method == 'update' and len(arguments) == 2:
                            d = json.loads(arguments[1])
                            for k, v in d.items():
                                pass
                        else:
                            line = method + ' ' + model + ' ' + arguments
                        # print('custom line:', line)
        return line

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        exit()

    def do_EOF(self, args):
        """Exit program when receiving Ctrl+D\n"""
        print()
        exit()

    def do_create(self, args):
        """Create a BaseModel, save it to a file, and print it's id\n"""
        if not args:
            print('** class name missing **')
            return
        elif args == 'BaseModel':
            b = BaseModel()
        elif args == 'User':
            b = User()
        elif args == 'Review':
            b = Review()
        elif args == 'Place':
            b = Place()
        elif args == 'Amenity':
            b = Amenity()
        elif args == 'City':
            b = City()
        elif args == 'State':
            b = State()
        else:
            print("** class doesn't exist **")
            return
        b.save()
        print(b.id)

    def do_show(self, args):
        """Print string repr of an instance based on class name and id\n"""
        if not args:
            print('** class name missing **')
            return
        args_arr = args.split(' ')
        if args_arr[0] not in self.model_names:
            print("** class doesn't exist **")
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = '.'.join(args_arr)
            if key not in models.storage.all():
                print('** no instance found **')
            else:
                print(models.storage.all()[key])

    def do_count(self, args):
        """Count instances of a specific class"""
        count = 0
        if not args:
            print('** class name missing **')
        elif args not in self.model_names:
            print("** class doesn't exist")
        else:
            for k in models.storage.all().keys():
                if k.startswith(args + '.'):
                    count += 1
        return count

    def do_destroy(self, args):
        """Delete and instance based on class name and id\n"""
        if not args:
            print('** class name missing **')
            return
        args_arr = args.split(' ')
        if args_arr[0] not in self.model_names:
            print("** class doesn't exist **")
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = '.'.join(args_arr)
            if key not in models.storage.all():
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, args):
        """Print string repr of instances\n"""
        if not args:
            for value in models.storage.all().values():
                print(value)
        else:
            if args not in self.model_names:
                print("** class doesn't exist **")
            else:
                for k, v in models.storage.all().items():
                    if k.startswith(args + '.'):
                        print(v)

    def do_update(self, args):
        """Update an instance based on class name and id\n
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not args:
            print("** class name missing **")
        else:
            args_arr = args.split(' ')
            nargs = len(args_arr)
            if args_arr[0] not in self.model_names:
                print("** class doesn't exist **")
            elif nargs < 2:
                print("** instance id missing **")
            elif '.'.join(args_arr[:2]) not in models.storage.all().keys():
                print("** no instance found **")
            elif nargs < 3:
                print("** attribute name missing **")
            elif args_arr[2] in ['id', 'created_at', 'updated_at']:
                pass
            elif nargs < 4:
                print("** value missing **")
            else:
                model = models.storage.all()['.'.join(args_arr[:2])]
                args_arr[3] = args_arr[3].strip('\"')
                if args_arr[3].isdigit():
                    args_arr[3] = int(args_arr[3])
                elif args_arr[3].isdecimal():
                    args_arr[3] = float(args_arr[3])
                setattr(model, args_arr[2], args_arr[3])

    def do_User(self, args):
        return self.do_all('User')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
