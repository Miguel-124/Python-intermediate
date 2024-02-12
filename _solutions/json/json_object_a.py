
def decoder(obj: dict) -> dict:
    clsname = obj.pop('species').capitalize()
    cls = globals()[clsname]
    return cls(**obj)


result = json.loads(DATA, object_hook=decoder)
