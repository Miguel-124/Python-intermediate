
result = """

SELECT `firstname`, `lastname`
FROM `users`
ORDER BY
    `lastname` ASC NULLS LAST,
    `firstname` DESC NULLS FIRST 

"""
