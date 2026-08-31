# /Users/robinvanicek/Documents/GitHub/test_GItHub/main.py

"""
Hlavní soubor
"""

############################################################
from pck1.pck2.users_directory import *
import debug
debug.module_name(__name__)

############################################################
print(f"Robinův věk je: {user_1.age}")
print(f"Robinova adresa je: {user_1.adress}")

print(dir(user_1))
