DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id        TEXT  PRIMARY KEY,
  name      TEXT  NOT NULL,
  email     TEXT  NOT NULL,
  username  TEXT  UNIQUE  NOT NULL,
  password  TEXT  NOT NULL
);

-- TODO: remove this, just added to quick fix test
INSERT INTO users (id, name, email, username, password) VALUES
("cccde22d-fe82-4146-b25c-c12c243c7d43", "test", "test@example.com", "test", "test");
