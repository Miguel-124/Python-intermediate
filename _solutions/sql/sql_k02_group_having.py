
result = """

SELECT `group`
FROM `users`
GROUP BY `group`
HAVING COUNT(`group`) >= 2

"""
