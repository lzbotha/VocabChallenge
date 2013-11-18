create table users(
    id SERIAL PRIMARY KEY,
    mxit_id VARCHAR(100) NOT NULL,
    username VARCHAR NOT NULL,
    joined DATE NOT NULL
);