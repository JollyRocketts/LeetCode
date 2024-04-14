(select u.name as results from Users u, MovieRating r where u.user_id=r.user_id group by u.name order by count(*) desc, u.name limit 1)

UNION ALL

(select m.title as results from Movies m, MovieRating r where m.movie_id=r.movie_id and r.created_at between '2020-02-01' and '2020-02-29' group by m.title order by avg(r.rating) desc, m.title limit 1)

