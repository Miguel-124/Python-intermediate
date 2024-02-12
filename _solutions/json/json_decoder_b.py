
class Decoder(json.JSONDecoder):
    def default(self, obj: dict) -> dict:
        for key, value in obj.items():
            if key in ('destination_landing', 'launch_date'):
                obj[key] = datetime.fromisoformat(value)
            elif key == 'birthdate':
                obj[key] = date.fromisoformat(value)
        return obj

    def __init__(self):
        super().__init__(object_hook=self.default)


result = json.loads(DATA, cls=Decoder)
