create table boards_statuses
(
    board_id  integer
        constraint boards_statuses_boards_id_fk
            references boards,
    status_id integer
        constraint boards_statuses_statuses_id_fk
            references statuses
);


