import sqlite3

connection = sqlite3.connect("vuln.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insert admin and regular user
# cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("admin", "admin", "admin"))
# cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("user", "user", "user"))

connection.commit()
connection.close()

print("Database initialized with users and roles.")