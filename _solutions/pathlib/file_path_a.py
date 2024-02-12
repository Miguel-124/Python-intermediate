
def result(filename):
    try:
        open(filename)
    except FileNotFoundError:
        print('File not found')
    else:
        print('Ok')


# Alternative Solution
from pathlib import Path

def result(filename):
    path = Path(filename)
    if path.exists():
        print('Ok')
    else:
        print('File not found')
