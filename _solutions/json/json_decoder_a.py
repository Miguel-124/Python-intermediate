
def decoder(obj: dict) -> dict:
    for key, value in obj.items():
        if key in ('destination_landing', 'launch_date'):
            obj[key] = datetime.fromisoformat(value)
        elif key == 'birthdate':
            obj[key] = datetime.fromisoformat(value).date()
    return obj


result = json.loads(DATA, object_hook=decoder)
