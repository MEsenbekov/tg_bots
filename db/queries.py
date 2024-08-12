# db/queries.py

CREATE_TABLE_REGISTRATION = """
CREATE TABLE IF NOT EXISTS registration (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL,
    firstname TEXT NOT NULL
);
"""

INSERT_INTO_TABLE_REGISTRATION = """
INSERT INTO registration (telegram_id, firstname) VALUES (?, ?)
"""
