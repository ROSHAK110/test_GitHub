# / Users / robinvanicek / Documents / GitHub / test_GItHub / pck1 / pck2
"""
Hlavní logika
"""


############################################################################
# Výpis informací souboru
def module_info() -> str:
    return f"{__name__}, {__doc__}"
# print(f"Module info: \n{module_info()}")

def mezera() -> None:
    print("\n\n")

############################################################################
from pck1.pck2.user import User

user_1= User(name= "Robin", age= 31, adress= "Staňkov", status="marryed")
user_2= User(name= "Kačka", age= 27, adress= "Staňkov", status="marryed")


print(user_1.name)
print(user_1.age)
print(user_1.adress)
# print(user_2.name)
# print(user_2.age)
# print(user_1.adress)
# mezera()

############################################################################
from debug import *

def print_info():
    module_name(__name__)
    module_doc(__doc__)

print_info()


