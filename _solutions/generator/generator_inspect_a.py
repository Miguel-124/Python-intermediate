
def function(data: list, species: str):
    result = []
    for *features, label in data:
        if label == species:
            result.append(features)
    return result


def generator(data: list, species: str):
    for *features, label in data:
        if label == species:
            yield features
