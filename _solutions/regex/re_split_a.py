
paragraph = re.compile(r'</?p>')

for p in paragraph.split(TEXT):
    if p.startswith('We choose to go to the moon'):
        result = p
