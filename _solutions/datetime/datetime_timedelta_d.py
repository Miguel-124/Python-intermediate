
years, seconds = divmod(DATA.total_seconds(), YEAR)
months, seconds = divmod(seconds, MONTH)
days, seconds = divmod(seconds, DAY)
hours, seconds = divmod(DATA.seconds, HOUR)
minutes, seconds = divmod(seconds, MINUTE)

result = {
    'years': int(years),
    'months': int(months),
    'days': int(days),
    'hours': int(hours),
    'minutes': int(minutes),
    'seconds': int(seconds),
}
