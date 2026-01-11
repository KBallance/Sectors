import sys
import Utility


class Main:
    def __init__(self, args):
        args = Utility.capitalize_List(args)
        if args[1] == "-H" or "-HELP" or "--HELP":
            print(" Arguments: -G - enables gui, -D - enables debug mode")
        if "-G" in args:
            print("gui Enabled")
        if "-D" in args:
            print("debug enabled")
        return None
    
main = Main(sys.argv)

