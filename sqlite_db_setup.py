import sqlite3

conn = sqlite3.connect('rpg_database.db')
print("Opened database successfully")

conn.execute('''
CREATE TABLE character (
    id TEXT PRIMARY KEY, name TEXT
)
''')
conn.execute('''
CREATE TABLE attribute (
    id TEXT PRIMARY KEY, name TEXT, character_id TEXT,

    FOREIGN KEY(character_id) REFERENCES character(id)
)
''')
conn.execute('''
CREATE TABLE skill (
    id TEXT PRIMARY KEY, name TEXT, character_id TEXT,

    FOREIGN KEY(character_id) REFERENCES character(id)
)
''')
conn.execute('''
CREATE TABLE item (
    id TEXT PRIMARY KEY, name TEXT, character_id TEXT,

    FOREIGN KEY(character_id) REFERENCES character(id)
)
''')

print("Table created successfully")

conn.execute('''
INSERT INTO character (id, name)
    VALUES ('1', 'Character1')
''')

conn.execute('''
INSERT INTO item (id, name, character_id)
    VALUES ('1', 'i1', '1')
''')

print("Inserted values successfully")

conn.close()
