
from get_password import get_password
from sys import argv

def main():
    
    value = argv[1]

    get_password(value)

try:
    num = int(argv[1])
except ValueError:
    print("argument must be a numeric value")
except IndexError:
    print("please enter an argument")
else:
    main()