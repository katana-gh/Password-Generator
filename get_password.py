
import secrets, random
import pyperclip

# get password  function

def get_password(length: int):

    length = int(length)
    if length < 12:
        length = 12
    elif length > 128:
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
    
    shuffled_password = ""

    for char in password:
        shuffled_password += char
    
    pyperclip.copy(shuffled_password)

