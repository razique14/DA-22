select * from customer;

-- limit and offset 
select * from customer order by first_name ;
select * from customer order by first_name limit 5;
select * from customer order by first_name limit 5 and offset 3;

--  fetch 

select * from customer order by first_name fetch first 5 rows only;


select * from customer order by first_name fetch next 5 rows only;


select * from customer order by first_name offset 5 fetch first 5 rows only;

select customer_id,
rental_id,
return_date
from rental
where 
customer_id = 1 or customer_id = 2
order by return_date desc

--=;...<<<>>>

select 
'foo' like 'foo' as one;   --true
'foo' like 'f%'  as two; --true
'foo' like '_o_'  as three; --true
'foo' like  'b_'  as four; --false 

--'her%'

--'%er%'

--like ~~
--ilike ~~ +76r0c/   f-+-*
--not like !~~
--not like !~~*


create table contacts(
id serial,
first_name varchar (50) not null,
last_name varchar (50) not null,
email_name varchar (250) not null,
phone varchar (15),
primary key (id)
);
select * from contacts

insert into contacts(first_name, last_name, email_name, phone)
values('John','Due','john.due@example.com',null),
('Lilly','Bush','lilly.bush@example.com','(264-545-5635)');

select * from contacts where phone = null;

select * from contacts where phone isnull;

drop table if exists courses;

-------------------------------------------------------------------------------------------------------------
create table courses(
course_id serial primary key,
course_name varchar (255) not null,
description varchar(500),
published_date date 
);


insert into 
(course_name,description,published_date);

VALUES
	('PostgreSQL for Developers','A complete PostgreSQL for Developers','2020-07-13'),
	('PostgreSQL Admininstration','A PostgreSQL Guide for DBA',NULL),
	('PostgreSQL High Performance',NULL,NULL),
	('PostgreSQL Bootcamp','Learn PostgreSQL via Bootcamp','2013-07-11'),
	('Mastering PostgreSQL','Mastering PostgreSQL in 21 Days','2012-06-30');
	
	
select * from courses

update courses
set published_date = '2022-1-1'
where course id = 2;

update courses
set description = 'adv.level postgresql'
where course id = 3;
returning *

select * from courses

-- delete the values -- it will delete everything 

delete from courses
where course_id = 3
returning*


alter table  courses
add column phone1 varchar(20),
add column phone2 varchar(20)

update courses
set phone1 ='9876544321',phone2 ='1234566789'
where course_id = 1
returning *

update courses
set phone1 ='9876576321',phone2 ='1234566789'
where course_id = 2
returning *

update courses
set phone1 ='9876124321',phone2 ='1237666789'
where course_id = 3
returning *

update courses
set phone1 ='5676544321',phone2 ='7634566789'
where course_id = 4
returning *

alter table courses
drop column phone1,
drop column phone2;

alter table courses
alter column course_name type varchar(200);

select * from courses; 

--usage of cascade