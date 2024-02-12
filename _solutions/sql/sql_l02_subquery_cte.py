
result = """

WITH `groups` AS (
    SELECT `group`
    FROM `users`
    GROUP BY `group`
    HAVING COUNT(`group`) >= 2
)

SELECT `firstname`, `lastname`
FROM `users`
WHERE `group` IN `groups`

"""
