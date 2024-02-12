
def search(pattern):
    if r := re.search(pattern, TEXT):
        return r.span()

a = search('Neil Armstrong')
b = search('Buzz Aldrin')
c = search('Michael Collins')
d = search('July 21 at 02:56 UTC')
e = search('Tranquility Base')
f = search('Mark Watney')
