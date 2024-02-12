
def myrange(*args, **kwargs):
    if kwargs:
        raise TypeError('myrange() takes no keyword arguments')

    start = ...
    stop = ...
    step = ...

    match len(args):
        case 3:
            start = args[0]
            stop = args[1]
            step = args[2]
        case 2:
            start = args[0]
            stop = args[1]
            step = 1
        case 1:
            start = 0
            stop = args[0]
            step = 1
        case 0:
            raise TypeError('myrange expected at least 1 argument, got 0')
        case _:
            n = len(args)
            raise TypeError(f'myrange expected at most 3 arguments, got {n}')


    current = start
    result = []

    while current < stop:
        result.append(current)
        current += step

    return result


## Alternative solution
# match len(args):
#     case 3: start, stop, step = args
#     case 2: (start, stop), step = args, 1
#     case 1: start, stop, step = 0, args, 1
#     case 0: raise TypeError('myrange expected at least 1 argument, got 0')
#     case _: raise TypeError(f'myrange expected at most 3 arguments, got {len(args)}')
