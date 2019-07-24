create table boards
(
	id serial not null
		constraint boards_pkey
			primary key,
	title text
);

