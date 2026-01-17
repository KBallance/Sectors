import sys
import Utility
from Relations import Relations


class Main:
    def __init__(self, args):
        args = Utility.capitalize_List(args)
        if "-H" or "-HELP" or "--HELP" in args:
            print(" Arguments: -G - enables gui, -D - enables debug mode")
        if "-G" in args:
            print("gui Enabled")
        if "-D" in args:
            print("debug enabled")
        return None
    
main = Main(sys.argv)

relation = Relations("Sources.txt")
relation.loopSources()

