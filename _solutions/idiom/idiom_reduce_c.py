
def myreduce(function, iterable):
    result = iterable[0]

    for current in iterable[1:]:
        result = function(result, current)

    return result
