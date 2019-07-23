create table cards
(
	id integer not null
		constraint cards_pkey
			primary key,
	board_id integer
		constraint cards_board_id_fkey
			references boards,
	title text not null,
	status_id integer
		constraint cards_status_id_fkey
			references statuses,
	"_order" integer
);

