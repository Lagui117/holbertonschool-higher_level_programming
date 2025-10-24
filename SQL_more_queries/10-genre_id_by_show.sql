-- Task 10: List all shows that have at least one genre
-- Output: tv_shows.title, tv_show_genres.genre_id
-- Sort by title ASC then genre_id ASC
-- Only one SELECT

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
