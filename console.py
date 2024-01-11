#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project."""
    prompt = "(hbnb) "
    dict_of_failure_output = { 1 : "** class name missing **", 2 : "** class doesn't exist **", 3 : "** instance id missing **", 4 : "** no instance found **" }
    def do_create(self, arg):
        if arg == "BaseModel":
            new_base_model = BaseModel()
            new_base_model.save()
            print("{}".format(new_base_model.id))
        else:
            if not arg:
                print("class name missing")
            else:
                print("class doesn't exist")
    def check(self, arg):
        if not arg:
            return 1
        else:
            args = arg.split()
            length = len(arg.split())
            if length == 1 and args[0] != "BaseModel":
                return 2
            elif length == 1:
                return 3
            else:
                arg = '.'.join(args) 
                data = storage.all()
                for key in data.keys():
                    if key == arg:
                        return arg
                return 4
    def do_show(self, arg):
        checked = self.check(arg)
        if type(checked) is int:
            print(self.dict_of_failure_output[checked])
        else:
            print (storage.all()[checked])
    def do_destroy(self, arg):
        checked = self.check(arg)
        if type(checked) is int:
            print(self.dict_of_failure_output[checked])
        else:
            del storage.all()[checked]
            storage.save()
    def do_all(self, arg):
        if arg == "BaseModel":
            string_repr_of_a_class = []
            for key in storage.all().keys():
                k , v = key.split('.')
                if k == arg:
                    string_repr_of_a_class.append(str(storage.all()[key]))
            print(string_repr_of_a_class)
        else:
            print("** class doesn't exist **")
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
