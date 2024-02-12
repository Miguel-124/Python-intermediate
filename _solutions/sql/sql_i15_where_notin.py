
result = """

SELECT `firstname`, `lastname`
FROM `users`
WHERE `group` NOT IN ('users', 'admins')

"""
