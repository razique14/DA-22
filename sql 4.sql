drop table if exists basket_a
drop table if exists basket_b
create table basket_a(
    a int primary key,
    fruits_a VARCHAR(100) NOT NULL
);


create table basket_b(
    b int primary key,
    fruits_b VARCHAR(100) NOT NULL
);

INSERT INTO basket_a (a,fruits_a)
values 
      (1, 'apple'),
	  (2,  'orange'),
	  (3, 'banana'),
	  (4, 'cucumber');
	  
	  
INSERT INTO basket_b (b,fruits_b)
values 
      (1, 'apple'),
	  (2,  'orange'),
	  (3, 'lichi'),
	  (4, 'pear');
	  
select * from basket_a;

select * from basket_b;


--- inner join-----

select a,fruits_a, b,fruits_b
from basket_a
inner join basket_b
on fruits_a = fruits_b;

------left join-----

select a , fruits_a  , b, fruits_b
from basket_a
left join basket_b
on fruits_a = fruits_b;

-------right join-----

select a , fruits_a  , b, fruits_b
from basket_a
right join basket_b
on fruits_a = fruits_b;


---------left outer join-----

select a , fruits_a  , b, fruits_b
from basket_a
left outer join basket_b
on fruits_a = fruits_b;


--------full join------

select a , fruits_a  , b, fruits_b
from basket_a
full join basket_b
on fruits_a = fruits_b


select a , fruits_a  , b, fruits_b
from basket_a
full join basket_b
on fruits_a = fruits_b
where fruits_a is null;


-------disjoint join-------

select a , fruits_a  , b, fruits_b
from basket_a
full join basket_b
on fruits_a = fruits_b


-----------cross join ------

drop table if exists t1 

create table t1(label char(1) primary key )


drop table if exists t2

create table t2(score int primary key )



insert into t1 (label)
values
     ('A'),
	 ('B');
	 
insert into t2 (score)
values
     ('1'),
	 ('2'),
	 ('3'),
	 ('4');
	 
select * from t1
select * from t2

select * from t1 croos join t2;

-----------==-===-=----===----------------------============================---------------------

drop table if exists most_popular_films

create table  most_popular_films(
    title varchar not null,
    release_year smallint
);

drop table if exists top_rated_films

create table  top_rated_films(
    title varchar not null,
    release_year smallint
);


insert into 
  top_rated_films(title,release_year)
 values
  ('the shawshank redemption',1994),
  ('the godfather',1972),
  ('12 angry men',1957);
  
 
insert into 
  most_popular_films(title,release_year)
  values
  ('the american pickle', 2020),
  ('the godfather',1972),
  ('greyhound',2020);
    

select * from  top_rated_films
union 
select * from  most_popular_films


select * from  top_rated_films
union all
select * from  most_popular_films


select * from  top_rated_films
intersect
select * from  most_popular_films

------group by------------

select * from payment

select customer_id, sum(amount) from payment
group by customer_id order by sum(amount) desc;


select customer_id, count(amount) from payment
group by customer_id order by sum(amount) desc;


select customer_id, aggregate (amount) from payment
group by customer_id order by sum(amount) desc;


-------having clause----------

select customer_id, sum(amount) from payment
group by customer_id having sum(amount)< 200 order by sum (amount) desc;


select customer_id, count(amount) from payment
group by customer_id having sum(amount) > 300 order by sum (amount) desc;

--------Subquery------------------

select * from film; 

select avg(rental_rate) from film;

select film_id,title,description,rental_rate 
from film 
where rental_rate > (
select avg(rental_rate) from film
);

----get films  that have the returned date between 2005-05-29   and 2005-05-30
----using film and inventary tables 

select * from film;
select * from rental;
select * from inventory;

select inventory.film_id,rental.return_date  
from rental  inner join inventory on inventory.inventory_id = rental.inventory_id
where return_date between '2005-05-29' and '2005-05-30'

select * from film;

select film_id,title,description from film
where film_id in 
(select inventory.film_id from rental
 inner join inventory on inventory.inventory_id = rental.inventory_id
 where return_date between '2005-05-29' and '2005-05-30'
 
);

-------- common table expressions ------- or ------- window functions --------

with duration as (
select film_id,title,description,(
case
    when length <40 then 'short'
    when length <90 then 'medium'
	else 'long'
end
)  as length from film
  )
select film_id,length,title,description
from duration
where length = 'long'
order by film_id;
