-- Task 12: List all shows with no linked genre
-- Output: tv_shows.title, tv_show_genres.genre_id (will be NULL)
-- Sort by title ASC, genre_id ASC
-- Only one SELECT

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
