-- Task 14: List all genres of the show "Dexter"
-- Output: tv_genres.name
-- Sort by tv_genres.name ASC
-- Only one SELECT

SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
