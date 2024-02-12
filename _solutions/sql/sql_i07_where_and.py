
result = """

SELECT `firstname`, `lastname`, `birthdate`
FROM `users`
WHERE `birthdate` >= '1990-01-01'
  AND `birthdate` <= '2000-01-01'

"""
