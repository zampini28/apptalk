DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id        TEXT    PRIMARY KEY,
  name      TEXT    NOT NULL,
  email     TEXT    NOT NULL,
  username  TEXT    UNIQUE    NOT NULL,
  password  TEXT    NOT NULL
);
