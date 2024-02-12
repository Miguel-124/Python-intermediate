
pattern = r'\d{2}:\d{2} UTC'
result = re.search(pattern, TEXT).group()
