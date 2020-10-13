-- Manager wants to see what has been happening to the inventory last day
SELECT * 
FROM Inventory 
WHERE timeSold 
BETWEEN '2020-08-19 00:00:00' AND '2020-08-19 23:59:00';

-- Manager wants to see how many times did Roberto sold last day
SELECT COUNT(employeeID) AS NUMBER_TIMES_THE_EMPLOYEE_SOLD
FROM Inventory
WHERE timeSold
BETWEEN '2020-08-19 00:00:00' AND '2020-08-19 23:59:00'
AND employeeID = 2;

-- Manager wants to see Roberto's selling records over time
SELECT *
FROM Inventory
WHERE employeeID = 2;

-- if Manager wants to see how much is left for each item i.e WATER BOTTLE
SELECT available
FROM Inventory
WHERE iid = 4;

-- if Manager wants to see who has sold Hershey's the last day
SELECT CONCAT(first,' ', last) AS employeeName
FROM Employee, Inventory
WHERE Employee.id = Inventory.employeeID
AND Inventory.iid = 1
AND timeSold BETWEEN '2020-08-19 00:00:00' AND '2020-08-19 23:59:00';