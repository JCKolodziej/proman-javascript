create table users
(
    id       serial not null
        constraint users_pkey
            primary key,
    login    text
        constraint users_login_key
            unique,
    password text
);


INSERT INTO public.users (id, login, password) VALUES (2, 'a', 'a');
INSERT INTO public.users (id, login, password) VALUES (3, 'b', 'b');