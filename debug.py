#/Users/robinvanicek/Documents/GitHub/test_GItHub

"""
Python soubor sloužící jako pomocník ke trasování při volání balíčků
"""

######################################################
import time

def start_pack(name: str) -> None:
    """
    Vstupuje do py souboru __init__
    :param name: name
    :return: str
    """
    print(f"právě se vstoupilo do balíčku {name}"\
           "\n\n###############################################")

def stop_pack(name: str) -> None:
    """
    Vystupuje z py souboru __init__
    :param name: name
    :return: str
    """
    print(f"právě se ukončilo procházení balíčku {name}" \
           "\n\n###############################################")


def module_name(name):
    """Tiskne zadaný název modulu"""
    print(f"Nacházíme se v modulu: {name}\n")

def module_doc(doc):
    """Tiskne dokumentační komentář modulu"""
    print(f"Popis modulu:", end="")
    print(f"{doc}\n")
