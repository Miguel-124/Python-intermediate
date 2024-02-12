
def convert(line):
    ip, *hosts = line.split()
    return {'ip':ip, 'hosts':hosts}


result = map(convert, DATA.splitlines())
