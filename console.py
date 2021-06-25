#!/usr/bin/python3
"""module of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Representation of a HBNBCommand"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
