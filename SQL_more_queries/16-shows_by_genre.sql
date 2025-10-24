-- Task 16: List all shows and their genres
-- Output: tv_shows.title, tv_genres.name
-- Show NULL for genre if a show has no genre
-- Sort by tv_shows.title ASC, tv_genres.name ASC
-- Only one SELECT

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
