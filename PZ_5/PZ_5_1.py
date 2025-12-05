# Составить функцию, которая напечатает сорок любых символов.

import random

def print_forty_chars():
    chars = "!@#$%^&*()_+qwertyuiop[]asdfghjkl;'zxcvbnm,./123457890-="
    result = random.choices(chars, k = 40)
    print(''.join(result))

print_forty_chars()

    