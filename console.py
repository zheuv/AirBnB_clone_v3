#!/usr/bin/python3
""" aihbnb cmd """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "Amenity",
               "City", "State", "Review"]
    dict_of_failure_output = {1: "** class name missing **",
                              2: "** class doesn't exist **",
                              3: "** instance id missing **",
                              4: "** no instance found **"}

    def do_create(self, arg):
        """ creates an instance """
        if arg in self.classes:
            arg = eval(arg)
            new_base_model = arg()
            new_base_model.save()
            print("{}".format(new_base_model.id))
        else:
            if not arg:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def check(self, arg):
        """ validates arg """
        if not arg:
            return 1
        else:
            args = arg.split()
            length = len(arg.split())
            if args[0] not in self.classes:
                return 2
            elif length == 1:
                return 3
            else:
                arg = []
                arg.append(args[0])
                arg.append(args[1])
                arg = '.'.join(arg)
                data = storage.all()
                for key in data.keys():
                    if key == arg:
                        return arg
                return 4

    def cast(self, arg):
        """cast string to float or int if possible"""
        try:
            if "." in arg:
                arg = float(arg)
            else:
                arg = int(arg)
        except ValueError:
            pass
        return arg

    def do_show(self, arg):
        """ show the string representation of an instance """
        checked = self.check(arg)
        if type(checked) is int:
            print(self.dict_of_failure_output[checked])
        else:
            print(storage.all()[checked])

    def do_destroy(self, arg):
        """ deletes an instance completely """
        checked = self.check(arg)
        if type(checked) is int:
            print(self.dict_of_failure_output[checked])
        else:
            del storage.all()[checked]
            storage.save()

    def do_all(self, arg):
        """ prints the string representation
        of all the instances of a class """
        if not arg:
            arg = "BaseModel"
        if arg in self.classes:
            string_repr_of_a_class = []
            for key in storage.all().keys():
                k, v = key.split('.')
                if k == arg:
                    string_repr_of_a_class.append(str(storage.all()[key]))
            print(string_repr_of_a_class)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ updates an instance's attribute """
        checked = self.check(arg)
        if type(checked) is int:
            print(self.dict_of_failure_output[checked])
        else:
            args = arg.split()
            if len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                if args[3].startswith('"'):
                    value = re.search(r'"([^"]+)"', arg).group(1)
                elif args[3].startswith("'"):
                    value = re.search(r'\'([^\']+)\'', arg).group(1)
                else:
                    value = arg[3]
                setattr(storage.all()[checked], args[2], self.cast(value))
                storage.save()

    def help(self):
        """ Prints help messages for all available commands. """
        commands = {
            'create': 'Creates a new instance of a specified class.',
            'show': 'Prints the string representation of an instance.',
            'destroy': 'Deletes an instance completely.',
            'all': 'Prints the string representation of all '
            'instances of a class.',
            'update': 'Updates an instance attribute.',
            'quit': 'Quit the command interpreter.',
            'EOF': 'Exit the program gracefully on EOF.'}

        for cmd, desc in commands.items():
            print(f"{cmd}: {desc}")
        print(
            "Use <command> -h or <command> --help for "
            "specific command usage."
        )

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the program gracefully on EOF."""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
