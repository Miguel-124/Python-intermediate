
result = map(datetime.fromisoformat, DATA)

# Alternative
result = [datetime.fromisoformat(x) for x in DATA]
