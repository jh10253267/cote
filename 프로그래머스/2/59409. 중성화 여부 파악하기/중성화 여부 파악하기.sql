SELECT ANIMAL_ID, NAME, CASE SEX_UPON_INTAKE
WHEN 'Neutered Male' 
THEN 'O' WHEN 'Spayed Female' THEN 'O' ELSE 'X' END AS '중성화'
FROM animal_ins ORDER BY animal_id