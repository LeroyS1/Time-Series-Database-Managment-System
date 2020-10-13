# This file will creat databases and all the tables
# Database: SUPERMARKET
# Tables: Inventory, ItemInfo, Employee, Customer
import mysql.connector
from mysql.connector import Error

def CreateDB():
     """Connect to MySQL database"""
     conn = None
     try:
          conn = mysql.connector.connect(host='localhost',
                                        user='root',
                                        password='nguyenA1$')
          if conn.is_connected():
               print('Connected to MySQL database')
          Cursor = conn.cursor()
          Cursor.execute("DROP DATABASE IF EXISTS SUPERMARKET;")
          Cursor.execute("CREATE DATABASE IF NOT EXISTS SUPERMARKET;")
          Cursor.execute("")
          Cursor.close()
          conn.close()
     except Error as e:
          print(e)

def CreateTables():
     """Connect to MySQL database"""
     conn = None
     try:
          conn = mysql.connector.connect(host='localhost',
                                        database='SUPERMARKET',
                                        user='root',
                                        password='nguyenA1$')
          if conn.is_connected():
               print('Connected to MySQL database')
          Cursor = conn.cursor()
          Cursor.execute("DROP TABLE IF EXISTS Inventory;")
          Cursor.execute("DROP TABLE IF EXISTS Employee;")
          Cursor.execute("DROP TABLE IF EXISTS ItemInfo;")
          Cursor.execute("DROP TABLE IF EXISTS Customer;")
          Cursor.execute("CREATE TABLE Employee(id INT NOT NULL, -- INT a medium integer and the NOT NULL constraint enforces a column to NOT accept NULL values.
                                        last VARCHAR(20) NOT NULL, -- VARCHAR(size): A VARIABLE length string (can contain letters, numbers, and special characters). 
                                        first VARCHAR(20) NOT NULL,
                                        salary INT NOT NULL,
                                        sex ENUM ('M','F') NOT NULL, -- ENUM: A string object that can have only one value, chosen from a list of possible values. 
                                        dob DATE NOT NULL, -- DATE: A date. Format: YYYY-MM-DD.
                                        dateStarted DATE NOT NULL,
                                        timeStarted TIME, -- A time. Format: hh:mm:ss
                                        /*The PRIMARY KEY constraint uniquely identifies each record in a table. 
                                        Primary keys must contain UNIQUE values, and cannot contain NULL values.
                                        A table can have only ONE primary key; and in the table, this primary key can consist of single or multiple columns *
                                        */
                                        PRIMARY KEY(id)
                                   )ENGINE = INNODB;")
          Cursor.execute("")
          Cursor.close()
          conn.close()
     except Error as e:
          print(e)