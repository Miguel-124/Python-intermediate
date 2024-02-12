
result = """

SELECT `firstname`, `lastname`
FROM `users`
WHERE `group` IN (
    SELECT `group`
    FROM `users`
    GROUP BY `group`
    HAVING COUNT(`group`) >= 2
)

"""
