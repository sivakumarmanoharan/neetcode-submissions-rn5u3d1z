-- Write your query below
SELECT DISTINCT player_id, MIN(event_date) OVER (PARTITION BY player_id ORDER BY event_date) as first_login
FROM activity