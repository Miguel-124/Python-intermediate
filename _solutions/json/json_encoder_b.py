
class Encoder(json.JSONEncoder):
    def default(self, obj) -> str:
        if isinstance(obj, date | datetime):
            return obj.isoformat()


result = json.dumps(DATA, cls=Encoder)
