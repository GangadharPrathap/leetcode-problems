/* Write your PL/SQL query statement below */
with movie as (
    select title from (select m.title from movierating mr
    join movies m on m.movie_id=mr.movie_id
    where mr.created_at between '2020-02-01' and '2020-02-29'
    group by mr.movie_id, m.title
    order by avg(mr.rating) desc, m.title)
    where rownum<=1
),
temp as (
    select fname from (select u.name as fname from movierating mr
    join users u on u.user_id=mr.user_id
    group by mr.user_id,  u.name
    order by count(mr.rating) desc, u.name)
    where rownum<=1
)
select title as results from movie 
union all 
select fname as results from temp ;