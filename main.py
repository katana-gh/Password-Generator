
from get_password import get_password
from sys import argv


def main():
    if len(argv) > 2:
        try:
            length = int(argv[1])
            time = int(argv[2])

        except ValueError:
            print("Argument must be a numeric value")
        except IndexError:
            print("Please enter an argument")
        
        else:
            get_password(length, time)

    if len(argv) < 3:
        try:
            length = int(argv[1])
        
        except ValueError:
            print("Argument must be a numeric value")
        except IndexError:
            print("Please enter an argument")
        else:
            get_password(length, time=30)

if __name__ == "__main__":
    main()