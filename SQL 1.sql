select * from address;


select * from  city;


select * from language;

select name from language;
select district, city_id, postal_code from  address;

select * from customer;

-- to concatenate

select 
first_name || '' || last_name

from customer;

-- we can perform any arithematic operations by using select




select 2*3
select 76+545*(2+5-3)

-- we can also give alias names to the columns
-- select store_id as s_id from customer ;
-- we can use as or just give space


select disrtict dist from address;
 -- by doing so we just get the columns which contains the names
 

select 
first_name || '' || last_name as full_names from customer

-- order by satement 
-- order by give ascending by default 
select 
first_name || '' || last_name full_names

from customer 
order by fisrt_name;

-- to get the desceding order use 'desc' after the statement
select
first_name || '' || last_name full_names
from customer
order by first_name desc;

select
first_name || '' || last_name full_names
from customer
order by first_name desc ,last_name asc;

select 
first_name || '' || last_name full_names,
length(first_name || '' || last_name) as lenn

from customer
order by first_name  desc, last_name desc nulls first ;


-- to create the table we use create table 

create table dummy
(p1 varchar(50) not null,
 p2 varchar(20) not null,
 p3 serial primary key
);

-- to delete the table we can do drop table

drop table dummy


drop table if exists dum2;

-- DISTINCT STATEMENT

create table dum2(
id serial primary key,
first_name varchar(100) not null,
email varchar(50) not null 
);

-- insert statement 
-- used to insert the values in the columns

insert into dum2(first_name,email)
values('razique','razique@gmail.com'),
('kaif','kaif@gmail.com'),
('saif','mdsaif@gmail.com'),
('salman','sallu@gmail.com'),
('rehan','salik@gmail.com')

select * from dum2