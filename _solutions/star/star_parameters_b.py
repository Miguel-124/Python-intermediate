
def isnumeric(*args):
    if not args:
        return False

    for arg in args:
        if type(arg) not in (int, float):
            return False

    return True
