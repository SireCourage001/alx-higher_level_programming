--This script  lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
SELECT c.id, c.name, s.names
FROM cities AS c
JOIN states AS s
ON c.state_id = states.id
ORDER BY c.id;

