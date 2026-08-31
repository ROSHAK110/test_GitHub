# /Users/robinvanicek/Documents/GitHub/test_GItHub/pck1/pck2
"""
Třída "User" pro zadání informací uživatele
"""

##############################################################
from debug import *

start_pack(__name__)

class User:
    """
    Třída pro zápis dat uživatelů
    """
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress


stop_pack(__name__)
