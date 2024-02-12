
result = [{'species': species, 'mean': mean(*values)}
          for *values, species in DATA[1:]]

# Alternative Solution
result = []
for *values, species in DATA[1:]:
    result.append({'species': species, 'mean': mean(*values)})

# Alternative Solution
result = [{'species': y, 'mean': mean(*X)}
          for *X, y in DATA[1:]]
