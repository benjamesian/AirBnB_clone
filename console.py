#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """ custom cmd for air_bnb """

    prompt = "(hbnb) "

    def do_quit(self, args):
        exit()

    def do_EOF(self, args):
        print()
        exit()

    def do_help(self, args):
        """ updated help """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
