
def myrange(*args, **kwargs):
    if kwargs:
        raise TypeError('myrange() takes no keyword arguments')

    match args:
        case [start, stop, step]: pass
        case [start, stop]: step = 1
        case [stop]: start = 0; step = 1
        case []: raise TypeError('myrange expected at least 1 argument, got 0')
        case _: raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')

    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result
