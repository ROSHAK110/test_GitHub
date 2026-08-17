#/Users/robinvanicek/Documents/GitHub/test_GItHub

"""
Python soubor sloužící jako pomocník ke trasování při volání balíčků
"""

######################################################

def start_pack(name: str) -> str:
    """
    Vstupuje do py souboru __init__
    :param name: name
    :return: str
    """
    return f"právě se vstoupilo do balíčku {name}"\
           "\n\n###############################################"

def stop_pack(name: str) -> str:
    """
    Vystupuje z py souboru __init__
    :param name: name
    :return: str
    """
    return f"právě se ukončilo procházení balíčku {name}" \
           "\n\n###############################################"