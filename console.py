#!/usr/bin/python3
import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
