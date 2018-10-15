BULK
INSERT CSVTest
FROM 'C:\Users\angel\OneDrive\Documents\other\data_training\data\RawDelData.csv'
WITH
(
FIELDTERMINATOR = ',',
ROWTERMINATOR = '\n'
)

SELECT *
FROM CSVTest;

/*
SELECT AVG(TipAmount)
FROM Table1;
------------------------------------------------
SELECT AVG(TipAmount)
FROM Table1 t
WHERE TipAmount > 0;
------------------------------------------------
SELECT *
FROM Table1 t
WHERE TipAmount < 0;
------------------------------------------------
SELECT AVG(TipAmount), DeliveryDriver
FROM Table1
GROUP BY DeliveryDriver;
------------------------------------------------
SELECT AVG(OrderAmount)
FROM Table1;
------------------------------------------------
SELECT COUNT(*) [Count of Dels]
	,CAST(COUNT(*) AS FLOAT) / 1301 * 100 [Percentage]
	,t2.Area [Neighborhood]
FROM Table1 t
	JOIN Table2 t2
		ON t.Area = t2.[Key]
GROUP BY t2.Area
ORDER BY Percentage DESC;
------------------------------------------------
SELECT COUNT(*) [Count of Dels], Housing [Housing Type]
FROM Table1 t
GROUP BY Housing;
------------------------------------------------
SELECT CAST(COUNT(CashOrCredit_Tip) AS FLOAT) / 1301 * 100 [Percentage]
	,COUNT(CashOrCredit_Tip) [Count of Dels]
	,CashOrCredit_Tip [Tip Type]
FROM Table1 t
GROUP BY CashOrCredit_Tip;
------------------------------------------------
*/