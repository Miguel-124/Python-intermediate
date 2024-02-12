
result = """

CREATE TABLE IF NOT EXISTS `contacts` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `firstname` TEXT,
    `lastname` TEXT,
    `birthdate` DATE DEFAULT NULL
)

"""
