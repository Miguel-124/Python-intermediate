
def parse_line(line):
    d, t, lvl, msg = line.split(', ', maxsplit=3)
    d = date.fromisoformat(d)
    t = time.fromisoformat(t)
    dt = datetime.combine(d, t)
    return {'when':dt, 'level':lvl, 'message':msg}

result = map(parse_line, DATA.splitlines())



## Alternative solution
# result = []
#
# for line in DATA.splitlines():
#     d, t, lvl, msg = line.strip().split(', ', maxsplit=3)
#     d = date.fromisoformat(d)
#     t = time.fromisoformat(t)
#     dt = datetime.combine(d, t)
#     result.append({'when': dt, 'level': lvl, 'message': msg})


## Alternative solution
# result = [{'when': dt, 'level': lvl, 'message': msg}
#           for line in DATA.splitlines()
#           if (row := line.strip().split(', ', maxsplit=3))
#           and (d := date.fromisoformat(row[0]))
#           and (t := time.fromisoformat(row[1]))
#           and (lvl := row[2])
#           and (msg := row[3])
#           and (dt := datetime.combine(d,t))]


# Solution 1 (%%timeit -r 1000 -n 1000)
# 27.7 µs ± 1.93 µs per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)

# Solution 2 (%%timeit -r 1000 -n 1000)
# 28 µs ± 1.26 µs per loop (mean ± std. dev. of 1000 runs, 1,000 loops each)


## Alternative solution
# result = [
#     {'when': datetime.fromisoformat('T'.join(row[0:2])),
#      'level': row[-2],
#      'message': row[-1]}
#
#      for line in DATA.splitlines()
#      if (row := line.split(', ', maxsplit=3))
# ]

## Alternative solution
# result = [{'when': dt, 'level': row[-2], 'message': row[-1]}
#           for line in DATA.splitlines()
#           if (row := line.split(', ', maxsplit=3))
#           and (dt := datetime.fromisoformat('T'.join(row[0:2])))]
#
#

## Alternative solution
# result = [{'when': dt, 'level': row[2], 'message': row[3]}
#           for line in DATA.splitlines()
#           if (row := line.split(', ', maxsplit=3))
#           and (d := date.fromisoformat(row[0]))
#           and (t := time.fromisoformat(row[1]))
#           and (dt := datetime.combine(d,t))]
