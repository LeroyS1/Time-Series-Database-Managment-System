/*
- This statement will load data from local file into table
- Suppose the user have a .txt file in a folder of its own, 
     containing 1 record per line and separated by tabs and arranged in order as the columns listed in the table. 
     You can use LOAD statement to populate the table. For missing values, 
     The user can use NULL values and that should be represented by ‘\N’ in the text file.
- If you want to use, say, commas to separate columns, not tabs, add FIELDS TERMINATED BY ',' to the LOAD command
- If some columns in the data file is enclosed with, say, double quotes, you need to add OPTIONALLY ENCLOED BY '"' as well
*/
LOAD DATA LOCAL INFILE "~/Dropbox/WORKSTUDY- LEROY LE/SuperMarket Database Project/MySQL/data/inventory.del" INTO TABLE Sales
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';

LOAD DATA LOCAL INFILE "~/Dropbox/WORKSTUDY- LEROY LE/SuperMarket Database Project/MySQL/data/employee.del" INTO TABLE Employee
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';

LOAD DATA LOCAL INFILE "~/Dropbox/WORKSTUDY- LEROY LE/SuperMarket Database Project/MySQL/data/item.del" INTO TABLE ItemInfo
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';

LOAD DATA LOCAL INFILE "~/Dropbox/WORKSTUDY- LEROY LE/SuperMarket Database Project/MySQL/data/customer.del" INTO TABLE Customer
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"';

-- /*
-- - The INSERT INTO statement is used to insert new records in a table.
-- - The first way specifies both the column names and the values to be inserted:
     -- INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);

-- For example: 
-- Jane whose employeeID = 3 sold a Pillow whose iid = 3 with the price of $145. 
-- Customer paid by cash and now stock available for the item is 9.
-- We do not need to insert timeSold value because the time of item sold will automatically update as we declared in the schema.
-- */
INSERT INTO Sales(iid,price,paymentMethod,employeeID,available) VALUES ('3','145','CASH','2','9');


-- /* 
-- - Or if you are adding values for all the columns of the table, you do not need to specify the column names in the SQL query. 
-- */
-- --For example: we just hired a new employee, and we want to add her into the Employee table
INSERT INTO Employee VALUES ('8','Asim','Lugo','16','F','1997-02-15','2020-08-25','20:00:00');



-- /*
-- The UPDATE statement is used to modify the existing records in a table.
-- UPDATE Syntax:
-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;
-- */

-- -- For example: if our store is reducing price for 'Hershey's' which id = 1 from $12 to $10
UPDATE ItemInfo SET price = 10 WHERE id = 1;



-- /*
-- - The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.
-- - The ALTER TABLE statement is also used to add and drop various constraints on an existing table.
-- */

-- -- For example: if we want to add a column called 'zipcode' to Customer table, we do: 
ALTER TABLE Customer ADD zipcode VARCHAR(6);

-- -- or if we no longer need the column zipcode, we want to drop it:
ALTER TABLE Customer DROP COLUMN zipcode;

-- /*
-- The DELETE statement is used to delete existing records in a table.
-- DELETE Syntax:
-- DELETE FROM table_name WHERE condition;
-- */

-- -- For example, if we are no longer selling air conditioner which id = 2, we should delete them from the ItemInfo table:
DELETE FROM ItemInfo WHERE id = 2;

