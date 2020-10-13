import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from datetime import date, time, timedelta
# PrettyTable is a simple Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables
from prettytable import PrettyTable

def insertCustomer():
     db_config = read_db_config()
     conn = None

     # To handle connection errors, use the try statement 
     # and catch all errors using the errors.Error exception
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()
     
          # the prompts
          C_lastname= input("Enter Customer's last name: ")
          C_firstname = input("Enter Customer's first name: ")
          C_phonenumber = input("Enter Customer's phone number: ")

          # MySQL INSERT statement to insert Customers' info into Customer table
          Statement = ("INSERT INTO Customer(last,first,phoneNumber) VALUES(%s,%s,%s)")
          data = (C_lastname,C_firstname,C_phonenumber)
          Cursor.execute(Statement,data)

          conn.commit()
          Cursor.close()
          conn.close()
          print("Inserted Records")
          print('\n' * 5)
     except mysql.connector.ERROR as e:
          if e.errno == Error.ER_ACCESS_DENIED_ERROR:
               print("Something is wrong with your user name or password")
          elif e.errno == Error.ER_BAD_DB_ERROR:
               print("Database does not exist")
          else:
               print(e)
          conn.close()

def updateCustomer():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          #look up the customer in the table to check whether it exists or not
          C_id = searchCustomer()

          # prompts
          print("Enter new data for the Customer")
          C_lastname= input("Enter Customer's last name: ")
          C_firstname = input("Enter Customer's first name: ")
          C_phonenumber = int(input("Enter Customer's phone number: "))

          # SQL statement to update existing data in the table
          Statement = ("UPDATE Customer SET last=%s, first=%s, phoneNumber=%s WHERE id=%s")
          data = (C_lastname,C_firstname, C_phonenumber,C_id)
          Cursor.execute(Statement,data)

          conn.commit()
          Cursor.close()
          conn.close()
          print("Updated Records")
          print('\n' * 5)

     except mysql.connector.ERROR as e:
          if e.errno == Error.ER_ACCESS_DENIED_ERROR:
               print("Something is wrong with your user name or password")
          elif e.errno == Error.ER_BAD_DB_ERROR:
               print("Database does not exist")
          else:
               print(e)
          conn.close()

def deleteCustomer():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          C_id= int(input("Enter Customer to be deleted from the Customer table: "))
          Statement = ("DELETE FROM Customer WHERE id = %s")
          qry_del = (C_id,)
          Cursor.execute(Statement,qry_del)
          conn.commit()
          Cursor.close()
          conn.close()
          print("Deleted Records")
          print('\n' * 5)
     except mysql.connector.ERROR as e:
          if e.errno == Error.ER_ACCESS_DENIED_ERROR:
               print("your user name or password is wrong")
          elif e.errno == Error.ER_BAD_DB_ERROR:
               print("Database does not exist")
          else:
               print(e)
          conn.close()

def searchCustomer():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          C_id = input("Enter Customer ID: ")

          # SQL SELECT statement to lookup customer by id
          Statement = ("SELECT * FROM Customer WHERE id=%s")
          Cursor.execute(Statement,(C_id,))
          data = Cursor.fetchall()

          # check whether the data exists or not
          # if not, returnID should be 0
          # if yes, print the table contains customer info and returnID = I_id 
          if not data:
               print("Could not find a record for this Customer")
               returnID = 0
          else:
               # add header for Pretty Table
               t = PrettyTable(['Customer Id', 'Last Name','First Name','Phone Number'])
               for row in data:
                    t.add_row([row[0],row[1],row[2],row[3]])
               print(t) 
               returnID = C_id

          input("Press any key to continue: ")

          #clear screen
          print('\n' * 5)
          conn.commit()
          Cursor.close()
          conn.close()
          return returnID

     except mysql.connector.ERROR as e:
          if e.errno == Error.ER_ACCESS_DENIED_ERROR:
               print("your user name or password is wrong")
          elif e.errno == Error.ER_BAD_DB_ERROR:
               print("Database does not exist")
          else:
               print(e)
          conn.close()

def showCustomerTable():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          # MySQL SELECT statement to look up all the customers
          Statement = ("SELECT * FROM Customer")
          Cursor.execute(Statement)
          data = Cursor.fetchall()

          # add header for Pretty Table
          t = PrettyTable(['Customer Id', 'Last Name','First Name','Phone Number'])
          for row in data:
               t.add_row([row[0],row[1],row[2],row[3]])
          print(t) 

          print("Found all records")
          input("Press any key to continue: ")
          print('\n' * 5)
          conn.commit()
          Cursor.close()
          conn.close()
     except mysql.connector.ERROR as e:
          if e.errno == Error.ER_ACCESS_DENIED_ERROR:
               print("your user name or password is wrong")
          elif e.errno == Error.ER_BAD_DB_ERROR:
               print("Database does not exist")
          else:
               print(e)
          conn.close()