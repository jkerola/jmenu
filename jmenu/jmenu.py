from utils import print_menu, parse_args
from time import time
from sys import argv, exit

if __name__ == "__main__":
    parse_args(argv)
    start = time()
    print_menu()
    print("Process took {:.2f} seconds.".format(time() - start))
    exit(0)
