import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from datetime import date, time, timedelta
# PrettyTable is a simple Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables
from prettytable import PrettyTable

def insertItem():
     db_config = read_db_config()
     conn = None
     try:
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          I_name= input("Enter Item name: ")
          I_price = int(input("Enter Item's price: "))
          I_stock= int(input("Enter number of the item in stock: "))

          #SQL Statement to insert data into table
          Statement = ("INSERT INTO ItemInfo(itemName,price,available) VALUES(%s,%s,%s)")
          data = (I_name,I_price,I_stock)

          #excute the command
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

def updateItem():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          #look up the item in the table to check whether it exists or not
          I_id = searchItem()

          # if the item does not exist in the table
          # otherwise, updating new data for this item
          if I_id != 0:
               print("Enter new data for this item")
               I_name= input("Enter Item name: ")
               I_price = input("Enter Item's price: ")
               I_stock= int(input("Enter number of the item in stock: "))

               # SQL statement to update existing data in the table
               Statement = ("UPDATE ItemInfo SET itemName=%s,price=%s,available=%s WHERE id=%s")
               data = (I_name,I_price, I_stock, I_id)
               Cursor.execute(Statement,data)
               print("Updated Records")

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

def deleteItem():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          # prompts
          I_id= int(input("Enter Item ID to be deleted from the item table: "))

          # MySQL DELETE statement to delete an item by id
          Statement = ("DELETE FROM ItemInfo WHERE id = %s")
          qry_del = (I_id,)
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

def searchItem():
     db_config = read_db_config()
     conn = None
     try:
          # connect MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          # the prompts
          I_id = input("Enter Product ID: ")

          # SQL SELECT statement to lookup item by its id
          Statement = ("SELECT * FROM ItemInfo WHERE id=%s")

          # execute the statement
          Cursor.execute(Statement,(I_id,))

          # fetch all data
          data = Cursor.fetchall()

          # check whether the data exists or not
          # if not, returnID should be 0
          # if yes, print the table contains itemInfo and returnID = I_id 
          if not data:
               print("Could not find a record for this Item")
               returnID = 0
          else:
               # add header for Pretty Table
               t = PrettyTable(['Item Id', 'Item Name','Price','Available'])
               for row in data:
                    t.add_row([row[0],row[1],row[2],row[3]])
               print(t)
               returnID = I_id

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

def showItemTable():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          # MySQL SELECT statement to look up all the items
          Statement = ("SELECT * FROM ItemInfo")
          Cursor.execute(Statement)
          data = Cursor.fetchall()

          # add header for Pretty Table
          t = PrettyTable(['Item Id', 'Item Name','Price','Available'])
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