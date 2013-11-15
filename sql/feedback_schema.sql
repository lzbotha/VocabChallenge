create table feedback(
	id integer primary key autoincrement,
	datetime text not null,
	username varchar not null,
	userid integer not null,
	feedback text
);