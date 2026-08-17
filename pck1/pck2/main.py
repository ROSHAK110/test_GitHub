# / Users / robinvanicek / Documents / GitHub / test_GItHub / pck1 / pck2
"""
Hlavní logika
"""

############################################################################
import debug

print("Jmenuji se Robin")

def module_info() -> tuple:
    return __name__, __doc__


print(module_info())