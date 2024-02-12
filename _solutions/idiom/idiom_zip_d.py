
def myzip(a, b, strict=False):
    times = min([len(a), len(b)])
    result = []

    if strict and len(a) != len(b):
        raise ValueError('zip() argument 2 is longer than argument 1')

    for i in range(times):
        row = (a[i], b[i])
        result.append(row)

    return result
