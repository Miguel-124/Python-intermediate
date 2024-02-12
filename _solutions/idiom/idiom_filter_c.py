
def is_numeric(x):
    return type(x) in (int,float)


result = filter(is_numeric, DATA)
