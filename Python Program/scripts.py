import os
from subprocess import call
import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config

print("Installing required packages...\n")
call('python -m pip install mysql-connector-python', shell=True)
call('pip install PrettyTable', shell=True)


print('\n' * 3)


print("Creating database and tables...\n")
db_config = read_db_config()
conn = None
try:
     conn = MySQLConnection(**db_config)
     Cursor = conn.cursor()

     #SQL Statement to insert data into table
     print("DROPPED DATABASE IF EXISTS SUPERMARKET\n")
     Cursor.execute("DROP DATABASE IF EXISTS SUPERMARKET")

     print("CREATED DATABASE IF NOT EXISTS SUPERMARKET\n")
     Cursor.execute("CREATE DATABASE IF NOT EXISTS SUPERMARKET")

     print("USED SUPERMARKET\n")
     Cursor.execute("USE SUPERMARKET")


     print("DROPPED TABLE IF EXISTS Sales\n")
     Cursor.execute("DROP TABLE IF EXISTS Sales")
     print("DROPPED TABLE IF EXISTS Employee\n")
     Cursor.execute("DROP TABLE IF EXISTS Employee")
     print("DROPPED TABLE IF EXISTS ItemInfo\n")
     Cursor.execute("DROP TABLE IF EXISTS ItemInfo")
     print("DROPPED TABLE IF EXISTS Customer\n")
     Cursor.execute("DROP TABLE IF EXISTS Customer")

     print("CREATED TABLE Employee\n")
     Cursor.execute("CREATE TABLE Employee(id INT NOT NULL AUTO_INCREMENT," 
                                             "last VARCHAR(20) NOT NULL, "
                                             "first VARCHAR(20) NOT NULL,"
                                             "salary INT NOT NULL,"
                                             "sex ENUM ('M','F') NOT NULL,"
                                             "dob DATE NOT NULL,"
                                             "timeWorks TIME,"
                                             "PRIMARY KEY(id))ENGINE = INNODB;")
     
     print("CREATED TABLE ItemInfo\n")
     Cursor.execute("CREATE TABLE ItemInfo(id INT NOT NULL AUTO_INCREMENT," 
                                             "itemName VARCHAR(50) NOT NULL, "
                                             "price DOUBLE NOT NULL,"
                                             "available INT NOT NULL,"
                                             "PRIMARY KEY(id))ENGINE = INNODB;")
     
     print("CREATED TABLE Customer\n")
     Cursor.execute("CREATE TABLE Customer(id INT NOT NULL AUTO_INCREMENT," 
                                             "last VARCHAR(20) NOT NULL, "
                                             "first VARCHAR(20) NOT NULL,"
                                             "phoneNumber BIGINT NOT NULL,"
                                             "PRIMARY KEY(id))ENGINE = INNODB;")
     
     print("CREATED TABLE Sales\n")
     Cursor.execute("CREATE TABLE Sales(timeSold DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP," 
                                             "iid INT, "
                                             "price DOUBLE NOT NULL,"
                                             "paymentMethod VARCHAR(20) NOT NULL,"
                                             "employeeID INT,"
                                             "available INT NOT NULL,"
                                             "FOREIGN KEY (iid) REFERENCES ItemInfo(id) ON UPDATE SET NULL ON DELETE SET NULL,"
                                             "FOREIGN KEY (employeeID) REFERENCES Employee(id) ON UPDATE SET NULL ON DELETE SET NULL)ENGINE = INNODB;")
     


     conn.commit()
     Cursor.close()
     conn.close()

     print('\n' * 5)
except mysql.connector.ERROR as e:
     if e.errno == Error.ER_ACCESS_DENIED_ERROR:
          print("Something is wrong with your user name or password")
     elif e.errno == Error.ER_BAD_DB_ERROR:
          print("Database does not exist")
     else:
          print(e)
     conn.close()
