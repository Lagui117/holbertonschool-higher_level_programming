-- Task 15: List all Comedy shows
-- Output: tv_shows.title
-- Sort by tv_shows.title ASC
-- Only one SELECT

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
