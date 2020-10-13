import mysql.connector
from mysql.connector import Error, MySQLConnection
from python_mysql_dbconfig import read_db_config
from datetime import date, time, timedelta
# PrettyTable is a simple Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables
from prettytable import PrettyTable

# insert Employee's information
def insertEmployee():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          # prompts
          E_lastname= input("Enter Employee's last name: ")
          E_firstname = input("Enter Employee's first name: ")
          E_salary = int(input("Enter Employee's salary: "))
          E_sex = input("Enter Employee's sex: ")

          print("Enter Employee's Date of Birth (Date/Month and Year) : ")
          MM = int(input("Enter Month : "))
          DD = int(input("Enter Day : "))
          YY = int(input("Enter Year : "))
          E_dob = date(YY,MM,DD)

          print("Enter Employee's Date of Started (Date/Month and Year) : ")
          MM = int(input("Enter Month : "))
          DD = int(input("Enter Day : "))
          YY = int(input("Enter Year : "))
          E_dateStarted = date(YY,MM,DD)

          print("Enter Employee's Time Works (Hours/Minute and Second) : ")
          HOR = int(input("Enter Hour : "))
          MIN = int(input("Enter Minute : "))
          SEC = int(input("Enter Second : "))
          E_timeWorks = time(HOR,MIN,SEC)

          # MySQL insert statement
          Statement1 = ("INSERT INTO Employee(last,first,salary,sex,dob,dateStarted,timeWorks) VALUES(%s,%s,%s,%s,%s,%s,%s)")
          data = (E_lastname,E_firstname,E_salary,E_sex,E_dob,E_dateStarted,E_timeWorks)
          
          # This script will excute the insert statment
          Cursor.execute(Statement1,data)
          
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

#update Employee's information
def updateEmployee():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          #look up the Employee in the table to check whether it exists or not
          E_id= searchEmployee()
    
          # prompts
          print("Enter new data for the Employee")

          E_lastname= input("Enter Employee's last name: ")
          E_firstname = input("Enter Employee's first name: ")
          E_salary = int(input("Enter Employee's salary: "))
          E_sex = input("Enter Employee's sex: ")

          print("Enter Employee's Date of Birth (Date/Month and Year) : ")
          MM = int(input("Enter Month : "))
          DD = int(input("Enter Day : "))
          YY = int(input("Enter Year : "))
          E_dob = date(YY,MM,DD)

          print("Enter Employee's Date of Started (Date/Month and Year) : ")
          MM = int(input("Enter Month : "))
          DD = int(input("Enter Day : "))
          YY = int(input("Enter Year : "))
          E_dateStarted = date(YY,MM,DD)

          print("Enter Employee's Time Works (Hours/Minute and Second) : ")
          HOR = int(input("Enter Hour : "))
          MIN = int(input("Enter Minute : "))
          SEC = int(input("Enter Second : "))
          E_timeWorks = time(HOR,MIN,SEC)

           # SQL statement to update existing data in the table
          Statement = ("UPDATE Employee SET last=%s,first=%s,salary=%s,sex=%s,dob= %s,dateStarted=%s,timeWorks=%s WHERE id=%s")
          data = (E_lastname,E_firstname,E_salary,E_sex,E_dob,E_dateStarted,E_timeWorks, E_id)
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

# delete Employee
def deleteEmployee():
     db_config = read_db_config()
     conn = None
     try:
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()
          E_id= int(input("Enter Employee ID to be deleted from the Employee table: "))
          Statement = ("DELETE FROM Employee WHERE id = %s")
          qry_del = (E_id,)
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

def searchEmployee():
     db_config = read_db_config()
     conn = None
     try:
          # connect to the MySQL database
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()

          E_id = input("Enter Employee ID: ")

          # SQL SELECT statement to lookup Employees by their id
          Statement = ("SELECT * FROM Employee WHERE id=%s")
          Cursor.execute(Statement,(E_id,))
          data = Cursor.fetchall()

          # check whether the data exists or not
          # if not, returnID should be 0
          # if yes, print the table contains Employee info and returnID = I_id 
          if not data:
               print("Could not find a record for this Employee")
               returnID = 0
          else:
                # add header for Pretty Table
               t = PrettyTable(['Employee Id', 'Last Name','First Name','Salary','Sex','DateOfBirth','Date Started','Time Works'])
               for row in data:
                    t.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
               print(t)
               returnID = E_id

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

def showEmployeeTable():
     db_config = read_db_config()
     conn = None
     try:
          conn = MySQLConnection(**db_config)
          Cursor = conn.cursor()
          Statement = ("SELECT * FROM Employee")
          Cursor.execute(Statement)
          data = Cursor.fetchall()
          # add header for Pretty Table
          t = PrettyTable(['Employee Id', 'Last Name','First Name','Salary','Sex','DateOfBirth','Date Started','Time Works'])
          for row in data:
               t.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
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