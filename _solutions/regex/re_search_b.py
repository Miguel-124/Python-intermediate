
pattern = r'<p>(We choose [a-zA-Z,. ]+)</p>'
result = re.search(pattern, TEXT).group(1)
