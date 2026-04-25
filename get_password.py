
import random
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
    password += random.choice(LOWER_CASE)
    password += random.choice(UPPER_CASE)
    password += random.choice(NUMS)
    password += random.choice(SYMBOLS)

    for i in range(1, length - 3):
        password += random.choice(character_list)
    shuffle_password = list(password)
    random.shuffle(shuffle_password)
    password = ""
    for random_char in shuffle_password:
        password += random_char
    pyperclip.copy(password)

