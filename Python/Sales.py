import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from datetime import date, time, datetime
import ItemInfo
# PrettyTable is a simple Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables
from prettytable import PrettyTable

def insertSales(EmployeeID):
     """
     This function help employees enter data into the database when they sold each item.
     """
     
     db_config = read_db_config()
     conn = None

     # To handle connection errors, use the try statement 
     # and catch all errors using the errors.Error exception
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          Item_ID = 0
          # lookup item info by ID from the ItemInfo table and then print it out
          Item_ID = ItemInfo.searchItem()

          if Item_ID != 0:
               # MySQL SELECT statement to look up the stock of the item
               Statement = ("SELECT available From ItemInfo WHERE id=%s")
               Cursor.execute(Statement,(Item_ID,))
               result = Cursor.fetchall()
               for row in result:
                    avai = row[0]

               if avai != 0: #check whether if the item is still available or not
                    # prompts 
                    price = input("Enter price is sold: ")
                    PaymentMethod = input("Enter Payment Method: ")
                    # whenever sold the item, the stock automatically decreases by 1
                    available = avai-1

                    # MySQL Update statement to update the stock of the item
                    Statement1 = ("UPDATE ItemInfo SET available = %s WHERE id = %s")
                    data = (available, Item_ID)
                    Cursor.execute(Statement1,data)

                    # MySQL INSERT statement to insert the item just sold into the Sales table
                    # These information will be stored in the Sales table over time sold
                    Statement2 = ("INSERT INTO Sales(iid,price,paymentMethod,employeeID,available) VALUES(%s,%s,%s,%s,%s)")
                    data = (Item_ID,price,PaymentMethod,EmployeeID,available)
                    Cursor.execute(Statement2,data)
                    print("Inserted Record")
               else:
                    print("This item is out of stock!")
               
          conn.commit()
          Cursor.close()
          conn.close()
          #inform the record is inserted to the table and clear the screen
          
          print('\n' * 5)

     except mysql.connector.ERROR as e:
          if e.errno == Error.ER_ACCESS_DENIED_ERROR:
               print("Something is wrong with your user name or password")
          elif e.errno == Error.ER_BAD_DB_ERROR:
               print("Database does not exist")
          else:
               print(e)
          conn.close()

def searchSalesByDate():
     """
     This function help employees look up information from Sales table by date.
     For example: you want to look up what has been happening to the inventory in the last day 
     """

     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()
     
          print("Enter Date From : ")
          MM = int(input("Enter Month : "))
          DD = int(input("Enter Day : "))
          YY = int(input("Enter Year : "))
          HOR = int(input("Enter Hour : "))
          MIN = int(input("Enter Minute : "))
          SEC = int(input("Enter Second : "))
          dateFROM = datetime(YY,MM,DD,HOR,MIN,SEC)

          print("Enter Date To : ")
          MM = int(input("Enter Month : "))
          DD = int(input("Enter Day : "))
          YY = int(input("Enter Year : "))
          HOR = int(input("Enter Hour : "))
          MIN = int(input("Enter Minute : "))
          SEC = int(input("Enter Second : "))
          dateTO = datetime(YY,MM,DD,HOR,MIN,SEC)

          #mySQL statement to look up data in the Sales table
          Statement = ("SELECT * FROM Sales WHERE timeSold BETWEEN %s AND %s")
          Cursor.execute(Statement,(dateFROM,dateTO,))
          data = Cursor.fetchall()
          
          if not data:
               print("Could not find a record for this Item")
          else:
               # add header for Pretty Table
               t = PrettyTable(['Time Sold', 'Item ID','Price Sold','Payment Method','Employee ID who sold the item','Available'])
               for row in data:
                    t.add_row([row[0],row[1],row[2],row[3],row[4],row[5]])
               print(t)

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

def searchSalesByEmployeeID():
     """
     This function help employees look up information from Sales table by EmployeeID.
     """

     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()
     
          E_id = input("Enter Employee ID to be searched: ")

          #mySQL statement to look up data in the Sales table
          Statement = ("SELECT * FROM Sales WHERE employeeID=%s")
          Cursor.execute(Statement,(E_id,))
          data = Cursor.fetchall()
          
          if not data:
               print("Could not find a record for this Employee")
          else:
               # add header for Pretty Table
               t = PrettyTable(['Time Sold', 'Item ID','Price Sold','Payment Method','Employee ID who sold the item','Available'])
               for row in data:
                    t.add_row([row[0],row[1],row[2],row[3],row[4],row[5]])
               print(t)

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

def printAllSalesTable():
     """
     This function help employees look up information from Sales table by EmployeeID.
     """

     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          #mySQL statement to look up data in the Sales table
          Statement = ("SELECT * FROM Sales")
          Cursor.execute(Statement,)
          data = Cursor.fetchall()
          
          if not data:
               print("Could not find a records")
          else:
               # add header for Pretty Table
               t = PrettyTable(['Time Sold', 'Item ID','Price Sold','Payment Method','Employee ID who sold the item','Available'])
               for row in data:
                    t.add_row([row[0],row[1],row[2],row[3],row[4],row[5]])
               print(t)
          
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