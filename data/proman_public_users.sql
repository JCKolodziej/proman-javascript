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

INSERT INTO public.users (id, login, password) VALUES (6, 'jc', '$2b$12$aI/WItvXMfj8HcCXQh1iOO/MaC38aGe7eo6J3lJm7muEnmOJLZ.ji');
INSERT INTO public.users (id, login, password) VALUES (7, 'dejv', '$2b$12$emg8wambmg/3LPIX1tBZou85OQpeELtMvS9umpDLblv4BJXqlr/mW');
INSERT INTO public.users (id, login, password) VALUES (8, 'izi', '$2b$12$MSlmxo/XNibBkYavf116xegMWOz0EU248f9F/6jSzKjEJ5AHYJNn2');