DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
);

INSERT INTO users (username, password, role) VALUES ('admin', 'admin', 'admin');
INSERT INTO users (username, password, role) VALUES ('user', 'user', 'user');
INSERT INTO users (username, password, role) VALUES ('username', 'password', 'user');
