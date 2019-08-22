create table statuses
(
    id    serial not null
        constraint statuses_pkey
            primary key,
    title text
);
