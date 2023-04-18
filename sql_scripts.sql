drop table if exists users cascade;
create table users (
id serial primary key,
username text not null,
registration_dt timestamp not null default CURRENT_TIMESTAMP
)

drop table if exists orders cascade;
create table orders (
id serial  primary KEY,
customer_id integer REFERENCES users (id),
courier_id integer REFERENCES users (id),
message text,
is_finished bool
)

drop table if exists events;
create table events (
id int  primary KEY,
order_id integer REFERENCES orders (id),
status text,
update_ts  timestamp not null default CURRENT_TIMESTAMP
)