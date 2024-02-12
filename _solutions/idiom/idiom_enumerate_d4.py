
result = []
header, *lines = DATA.splitlines()
header = header.strip().split(',')
nrows, ncols, *class_labels = header
result = dict(enumerate(class_labels))
