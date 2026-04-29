
import secrets, random
import pyperclip
import time
import platform

# get password  function

def get_password(length: int):
    is_windows = False
    is_ios = False

    if platform.system() == "iOS":
        is_ios = True
    else:
        is_windows = True

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
    if is_ios:
        print("Use cmd+v to paste")
    else:
        print("Use cntrl+v to paste")
    print()
    print("removing password in 25 seconds...")
    time.sleep(25)
    print()
    pyperclip.copy("")
    print("password removed from clipboard")

