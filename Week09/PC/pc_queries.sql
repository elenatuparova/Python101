SELECT AVG(SPEED) AS "AVERAGE SPEED"
FROM PC;

SELECT MAKER, AVG(SCREEN) AS "AVERAGE SCREEN SIZE"
FROM LAPTOP JOIN PRODUCT ON LAPTOP.MODEL=PRODUCT.MODEL
GROUP BY MAKER;

SELECT AVG(SPEED) AS "AVERAGE SPEED"
FROM LAPTOP
WHERE PRICE>1000;

SELECT HD, AVG(PRICE) AS "AVERAGE PRICE"
FROM PC
GROUP BY HD;

SELECT SPEED, AVG(PRICE) AS "AVERAGE PRICE"
FROM PC
GROUP BY SPEED
HAVING SPEED>500;

SELECT AVG(PRICE) AS "AVERAGE PRICE FOR MAKER A"
FROM PC JOIN PRODUCT ON PC.MODEL=PRODUCT.MODEL;

SELECT AVG(PRICE) AS "AVERAGE PRICE FOR MAKER B"
FROM (SELECT PRICE FROM PC JOIN PRODUCT ON PC.MODEL=PRODUCT.MODEL UNION SELECT PRICE FROM LAPTOP JOIN PRODUCT ON LAPTOP.MODEL=PRODUCT.MODEL);

SELECT MAKER, COUNT(DISTINCT PC.MODEL)
FROM PC JOIN PRODUCT ON PC.MODEL=PRODUCT.MODEL
GROUP BY MAKER;

SELECT MAKER
FROM PC JOIN PRODUCT ON PC.MODEL=PRODUCT.MODEL
GROUP BY MAKER
HAVING COUNT(DISTINCT PC.MODEL)>3;

SELECT MAKER
FROM PC JOIN PRODUCT ON PC.MODEL=PRODUCT.MODEL
WHERE PRICE=(SELECT MAX(PRICE) FROM PC);

SELECT AVG(HD) AS "AVERAGE HD SIZE"
FROM PC JOIN PRODUCT ON PC.MODEL=PRODUCT.MODEL
WHERE MAKER IN (SELECT MAKER FROM PRINTER JOIN PRODUCT ON PRINTER.MODEL=PRODUCT.MODEL);
