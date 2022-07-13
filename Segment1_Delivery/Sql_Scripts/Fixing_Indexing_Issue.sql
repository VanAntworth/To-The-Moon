--For setting the ID when it is out of sync - 
-- solution to the Error
-- ERROR:  duplicate key violates unique constraint

SELECT SETVAL((SELECT PG_GET_SERIAL_SEQUENCE('"Twitter_data"', 'ID')), (SELECT (MAX("ID") + 1) FROM "Twitter_data"), FALSE);