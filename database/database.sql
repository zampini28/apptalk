
-- default user
CREATE TABLE IF NOT EXISTS users(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT    NOT NULL,
    username    TEXT    UNIQUE  NOT NULL,
    email       TEXT    NOT NULL,
    password    TEXT    NOT NULL
);

---- user login token session
CREATE TABLE IF NOT EXISTS sessions(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    token   TEXT    NOT NULL,
    FOREIGN key (user_id) REFERENCES users(id)
);

-- gotta think more abt how to implement these

---- user contacts list
--CREATE TABLE IF NOT EXISTS user_contacts(
--    id      INTEGER PRIMARY KEY AUTOINCREMENT,
--    user_id INTEGER NOT NULL,
--    contact_id INTEGER NOT NULL,
--    FOREIGN key (user_id)    REFERENCES users(id),
--    FOREIGN key (contact_id) REFERENCES users(id),
--    unique (user_id, contact_id)
--);
--
---- user message 
--CREATE TABLE IF NOT EXISTS messages(
--    id          INTEGER     PRIMARY KEY AUTOINCREMENT,
--    sender_id   INTEGER     NOT NULL,
--    receiver_id INTEGER     NOT NULL,
--    content     TEXT        NOT NULL,
--    -- maybe hash key (?)
--    time        datetime    DEFAULT CURRENT_TIMESTAMP,
--    FOREIGN key (sender_id)    REFERENCES users(id),
--    FOREIGN key (receiver_id) REFERENCES users(id)
--);
