
header, *lines = DATA.splitlines()
nrows, ncols, *class_labels = header.strip().split(',')
result = dict(enumerate(class_labels))
