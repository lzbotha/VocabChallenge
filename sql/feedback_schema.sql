create table feedback(
	id SERIAL PRIMARY KEY,
	datetime TIMESTAMP NOT NULL,
	userid INT NOT NULL,
	feedback TEXT
);