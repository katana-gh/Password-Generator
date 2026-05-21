
from get_password import get_password
from sys import argv

def main():
    try:
        length = int(argv[1])
        
    except ValueError:
        print("argument must be a numeric value")
    except IndexError:
        print("Please enter an argument")
    else:
        get_password(length)

if __name__ == "__main__":
    main()