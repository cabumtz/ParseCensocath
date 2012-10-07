SELECT * FROM Encuesta WHERE Id = 19;

SELECT * FROM Encuesta;

SELECT Id, Fecha, DATE_FORMAT(Fecha, '%d/%m/%Y'), IdEncuestador, Observacion FROM Encuesta;

-- 2012-09-30
-- 2012-09-30T17:12:07
-- DATE_FORMAT(date,format)
SELECT DATE_FORMAT(CURRENT_TIMESTAMP(), '%d/%m/%Y');

SELECT STR_TO_DATE('01,5,2013','%d,%m,%Y');

SELECT * FROM Encuestador;


SHOW TABLES;

SELECT * FROM Familia;



DELETE FROM Encuesta;



ALTER TABLE Familia
    ADD COLUMN `Lote` VARCHAR(10) NULL;
	 
	 
	 
	 
	 
ALTER TABLE Familia
    DROP COLUMN `FechaEncuesta`;
	 
	 
SELECT * FROM Colonia;