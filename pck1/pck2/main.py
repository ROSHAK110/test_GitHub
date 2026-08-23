# / Users / robinvanicek / Documents / GitHub / test_GItHub / pck1 / pck2
"""
Hlavní logika
"""

############################################################################
# Výpis informací souboru
def module_info() -> str:
    return f"{__name__}, {__doc__}"
print(f"Module info: \n{module_info()}")

############################################################################
from user import User
user_1= User(name= "Robin", age= 31, adress= "Staňkov")
user_2= User(name= "Kačka", age= 27, adress= "Staňkov")

print(user_1.name)
print(user_2.age)
print(user_1.age)