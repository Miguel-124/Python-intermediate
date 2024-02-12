
def encoder(obj: Any) -> str:
    if isinstance(obj, date | datetime):
        return obj.isoformat()


result = json.dumps(DATA, default=encoder)
