create table boards
(
    id      serial not null
        constraint boards_pkey
            primary key,
    title   text,
    user_id integer
        constraint boards_user_id__fk
            references users
);


INSERT INTO public.boards (id, title, user_id) VALUES (1, 'board 1', null);
INSERT INTO public.boards (id, title, user_id) VALUES (9, 'public', null);
INSERT INTO public.boards (id, title, user_id) VALUES (14, 'private', 6);
