
def mean(*args):
    if not args:
        raise ValueError('At least one argument is required')
    return sum(args) / len(args)
