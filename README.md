# Time-Series-Database-Managment-System

### These are steps to run the program in the Python Program Folder.

1. Install MySQL to the local computer.
     1.1 Download MySQL Server with this link: https://dev.mysql.com/downloads/mysql/ 
     1.2 Install MySQL Server to your local computer and set up the root password for MySQL

2. Go to the file "config.ini", and then change the password = 'your root password'

3. Open Terminal and go to the program's directory and run:
     $ python3 scripts.py

	- This "scripts.py" will install the required packages for this program. 
     - It also will create empty databases and tables for the first time.

4. Then, if everything is good, just run:
     $ python3 MainMenu.py

5. Every time you want to run the program, you go to step 4. You do not need to run step 3 because if you run step 3 again, 
all the old databases, tables, and data will be overwritten.


*Notes: - This program like a toy for a time series database management system. This program is recommended for people who do not know anything about
          SQL or Python. They just need to enter data, search data, and update data through this program. They will not interact with any Python
          and SQL code.

      - If someone knows about SQL, they can use sql files in the MySQL folder. Those files contain MySQL statements


====================================================================================================

In the MySQL folder, there are files:
- "create.sql" contains example SQL statements and comments for creating databases and tables, or dropping databases and tables.

- "load.sql" contains example SQL statements and comments for 
		- loading data from local files into tables.
		- inserting data into tables.
		- updating the existing records in tables
		- altering table is used to add, delete, or modify columns in existing tables.
		- deleting existing records in tables.

- "queries.sql" contains example SQL statements and comments for querying data from tables.

- and data folder contains local data files for testing purposes if you want to use LOADING DATA LOCAL INFILE in the "load.sql" file.

**NOTE: all file formats in the data folder are ".del". You can use any other formats like .csv , .txt, ... 
          But make sure that the format of the data in those files should be exactly the same
