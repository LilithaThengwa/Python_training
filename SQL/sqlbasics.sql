-- SELECT * FROM movies
-- where id == 6

-- select * from movies
-- where year between 2000 and 2010

-- select * from movies 
-- where year not between 2000 and 2010

-- select * from movies 
-- where id < 6

-- select * from movies
-- where title like "%Toy Story%"

-- select * from movies
-- where director = "John Lasseter"

-- select * from movies
-- where director not like "John Lasseter"

-- select * from movies
-- where title like "WALL-%"

-- SELECT distinct director FROM movies
-- order by director asc

-- select * from movies
-- order by year desc
-- limit 4

-- select * from movies
-- order by title
-- limit 5

-- select * from movies
-- order by title
-- limit 5 offset 5

SELECT city, population FROM north_american_cities
where country like "Canada"

select * from north_american_cities
where country like "United States"
order by latitude desc

select * from north_american_cities
where longitude < -87.629798
order by longitude asc

select * from north_american_cities
where country like "mexico"
order by population desc
limit 2

select * from north_american_cities
where country like "united states"
order by population desc
limit 2 offset 2

-- ====================================================================================

-- SELECT title, domestic_sales, international_sales FROM boxoffice
-- join movies 
-- on movies.Id = boxoffice.movie_id

-- SELECT title, domestic_sales, international_sales FROM boxoffice
-- join movies 
-- on movies.Id = boxoffice.movie_id
-- where international_sales > domestic_sales

-- SELECT title, rating FROM boxoffice
-- join movies 
-- on movies.Id = boxoffice.movie_id
-- order by rating desc


-- ======================================================================================

-- SELECT distinct building from employees

-- SELECT * from buildings

-- select distinct building_name, role from buildings 
-- left join employees
-- on building_name = building;

-- =======================================================================================

-- select name, role from employees
-- where building is null

-- select distinct building_name from buildings 
-- left join employees
-- on buildings.building_name = empployees.building
-- where role is null

-- ========================================================================================

-- SELECT title, movie_id, (domestic_sales + international_sales)/1000000 as total
-- FROM movies
-- join boxoffice
-- on movies.id = boxoffice.movie_id

-- SELECT title, rating * 10 as total
-- FROM movies
-- join boxoffice
-- on movies.id = boxoffice.movie_id

-- select * from movies
-- where year % 2 = 0

-- ==========================================================================================

-- SELECT *, max(years_employed) FROM employees

-- select role, avg(years_employed) from employees
-- group by role

-- select building, sum(years_employed) from employees
-- group by building

-- ==========================================================================================

-- SELECT count() FROM employees
-- where role = "Artist"

-- SELECT role, count() FROM employees
-- group by role

-- select sum(years_employed) from employees
-- where role = "Engineer"

-- ===========================================================================================

-- select director, count(id) from movies
-- group by director

-- select director, sum(domestic_sales + international_sales) as total
-- from movies
-- join boxoffice
-- on movies.id = boxoffice.movie_id
-- group by director

-- ============================================================================================

-- insert into movies
-- values (4, "toy story 4", "John Doe", 2024, 81)

-- insert into boxoffice
-- values (4, 8.7, 340000000, 270000000)

-- =============================================================================================

-- update movies
-- set director = "John Lasseter"
-- where title = "A Bug's Life"

-- update movies
-- set year = 1999
-- where title = "Toy Story 2"

-- update movies
-- set title = "Toy Story 3",
-- director = "Lee Unkrich"
-- where id = 11

-- =============================================================================================

-- delete from movies
-- where year < 2005

-- delete from movies
-- where director = "Andrew Stanton"

-- ==============================================================================================

-- create table Database (
--     name TEXT,
--     version float,
--     Download_count INTEGER
-- )

-- ==============================================================================================

-- alter table movies
-- add Aspect_ratio float

-- alter table movies
-- add language text
-- default "english"

-- ==============================================================================================

drop table if exists movies

drop table if exists boxoffice