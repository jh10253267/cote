SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_OUTS O JOIN ANIMAL_INS I
ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE IN('Intact Male', 'Intact Female')
    AND O.SEX_UPON_OUTCOME IN('Spayed Female',
                              'Neutered Male',
                              'Spayed Male',
                             'Neutered Female')