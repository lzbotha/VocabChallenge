create table games(
    id SERIAL PRIMARY KEY,
    username VARCHAR NOT NULL,
    userid INT NOT NULL,
    score INT NOT NULL,
    hints INT NOT NULL DEFAULT 0
);