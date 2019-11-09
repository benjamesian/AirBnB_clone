#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """custom cmd for air_bnb"""

    prompt = "(hbnb) "

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
        elif args == 'BaseModel':
            b = BaseModel()
            b.save()
            print(b.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Print string repr of an instance based on class name and id\n"""
        if not args:
            print('** class name missing **')
            return
        args_arr = args.split(' ')
        if args_arr[0] not in ['BaseModel']:
            print("** class doesn't exist **")
        elif len(args_arr) == 1:
            print('** instance id missing **')
        else:
            key = '.'.join(args_arr)
            if key not in models.storage.all():
                print('** no instance found **')
            else:
                print(models.storage.all()[key])

    def do_destroy(self, args):
        """Delete and instance based on class name and id\n"""
        if not args:
            print('** class name missing **')
            return
        args_arr = args.split(' ')
        if args_arr[0] not in ['BaseModel']:
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
            if args not in ['BaseModel']:
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
            if args_arr[0] not in ['BaseModel']:
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
                if args_arr[3].startswith('\"'):
                    args_arr[3] = args_arr[3].strip('\"')
                setattr(model, args_arr[2], args_arr[3])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
