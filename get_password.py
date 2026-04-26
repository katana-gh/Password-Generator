
import secrets
import pyperclip

# get password  function

def get_password(length=int):
    length = int(length)
    if length < 12:
        length = 12
    elif length > 128:
        length = 128
    LOWER_CASE = "abcdefghijklmnopqrstuvwxyz"
    UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMS = "1234567890"
    SYMBOLS = "!@#$%^&*()_+-=[]{}|;:,./<>? "
    all_characters = LOWER_CASE + UPPER_CASE + NUMS + SYMBOLS
    character_list = []
    for char in all_characters:
        character_list.append(char)
    
    password = ""
    password += secrets.choice(LOWER_CASE)
    password += secrets.choice(UPPER_CASE)
    password += secrets.choice(NUMS)
    password += secrets.choice(SYMBOLS)

    for i in range(1, length - 3):
        password += secrets.choice(character_list)
    random_password = ""
    for i in password:
        random_password += secrets.choice(password)
    pyperclip.copy(random_password)

