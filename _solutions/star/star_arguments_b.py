
def myrange(*args, **kwargs):
    if kwargs:
        raise TypeError('myrange() takes no keyword arguments')
    if len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    elif len(args) == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 0:
        raise TypeError('myrange expected at least 1 argument, got 0')
    else:
        raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')

    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
