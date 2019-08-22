create table cards
(
    id        serial not null
        constraint cards_pkey
            primary key,
    board_id  integer
        constraint cards_board_id_fkey
            references boards
            on delete cascade,
    title     text   not null,
    status_id integer
        constraint cards_status_id_fkey
            references statuses
            on delete cascade,
    "_order"  integer,
    user_id   integer
        constraint cards_user_id_fkey
            references users
);


