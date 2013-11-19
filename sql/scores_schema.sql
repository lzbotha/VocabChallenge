create table scores(
    id SERIAL PRIMARY KEY,
    userid INT NOT NULL,
    language VARCHAR NOT NULL,
    score INT NOT NULL
);