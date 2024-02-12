
pattern = r'<p>(.*?)</p>'
for p in re.findall(pattern, TEXT):
    if p.startswith('We choose'):
        result = p
