
import secrets
import random
import pyperclip
import time
import platform

# get password  function

def get_password(length: int) -> str:
    is_ios = False

    is_ios = True if platform.system() == "iOS" else False

    length = int(length)
    if length < 12:
        print("password length too small, adjusting to nearest length: 12")
        length = 12
    elif length > 128:
        print("password length too big, adjusting to nearest length: 128")
        length = 128
    
    LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
    UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMS = "1234567890"
    SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,./<>? "
    character_list = LOWER_CASE + UPPER_CASE + NUMS + SYMBOLS
    
    password = ""
    password += secrets.choice(LOWER_CASE)
    password += secrets.choice(UPPER_CASE)
    password += secrets.choice(NUMS)
    password += secrets.choice(SYMBOLS)

    for i in range(length - 4):
        password += secrets.choice(character_list)

    password = list(password)
    r = random.SystemRandom()
    r.shuffle(list(password)), r.shuffle([5, 4]), r.shuffle(password)
    
    shuffled_password = "".join(password)


    
    print()

    pyperclip.copy(shuffled_password)
    print("password copied to clipboard")
    print()
    
    print("Use cmd+v to paste") if is_ios else print("Use cntrl+v to paste")
    
    print()
    counter = 25
    while counter > 0:
        print(f"Removing password in {counter} seconds...")
        time.sleep(1)
        counter -= 1
    
    pyperclip.copy("")
    print("password removed from clipboard")

if __name__ == "__main__":
    get_password()
