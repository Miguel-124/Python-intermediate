
def isnumeric(*args, **kwargs):
    args += tuple(kwargs.values())

    if not args:
        return False

    for arg in args:
        if type(arg) not in (float, int):
            return False

    return True
