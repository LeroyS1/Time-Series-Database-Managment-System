import Sales
import ItemInfo
import Employee
import Customer

def MenuSales(EmployeeID):
    while True:
        print("\t\t\t Sales Management\n")
        print("=================================================================")
        print("1. Sale")
        print("2. Search Record by Date")
        print("3. Search Record by Employee ID")
        print("4. Print all Sales data over time")
        print("5. Return to Main Menu")
        print("=================================================================")
        options = int(input("Enter between 1 to 5 -------> : "))
        if options == 1:
            Sales.insertSales(EmployeeID)
        elif options == 2:
            Sales.searchSalesByDate()
        elif options == 3:
            Sales.searchSalesByEmployeeID()
        elif options == 4:
            Sales.printAllSalesTable()
        elif options == 5:
            print('\n' * 5)
            return
        else:
            print("Wrong Choice.....Enter your options again")
            x = input("Enter any key to continue")

def MenuItemInfo():
     while True:
        print("\t\t\t ItemInfo Management\n")
        print("=================================================================")
        print("1. Insert ItemInfo Record")
        print("2. Search ItemInfo Record")
        print("3. Delete ItemInfo Record")
        print("4. Update ItemInfo Record")
        print("5. Show All ItemInfo Records")
        print("6. Return to Main Menu")
        print("=================================================================")
        options = int(input("Enter between 1 to 6 -------> : "))
        if options == 1:
            ItemInfo.insertItem()
        elif options == 2:
            ItemInfo.searchItem()
        elif options == 3:
            ItemInfo.deleteItem()
        elif options == 4:
            ItemInfo.updateItem()
        elif options == 5:
            ItemInfo.showItemTable()
        elif options == 6:
            print('\n' * 5)
            return
        else:
            print("Wrong Choice.....Enter your options again")
            x = input("Enter any key to continue")

def MenuEmployee():
     while True:
        print("\t\t\t Employee Management\n")
        print("=================================================================")
        print("1. Insert Employee Record")
        print("2. Search Employee Record")
        print("3. Delete Employee Record")
        print("4. Update Employee Record")
        print("5. Show All Employee Records")
        print("6. Return to Main Menu")
        print("=================================================================")
        options = int(input("Enter between 1 to 6 -------> : "))
        if options == 1:
            Employee.insertEmployee()
        elif options == 2:
            Employee.searchEmployee()
        elif options == 3:
            Employee.deleteEmployee()
        elif options == 4:
            Employee.updateEmployee()
        elif options == 5:
            Employee.showEmployeeTable()
        elif options == 6:
            print('\n' * 5)
            return
        else:
            print("Wrong Choice.....Enter your options again")
            x = input("Enter any key to continue")

def MenuCustomer():
     while True:
        print("\t\t\t Customer Management\n")
        print("=================================================================")
        print("1. Insert Customer Record")
        print("2. Search Customer Record")
        print("3. Delete Customer Record")
        print("4. Update Customer Record")
        print("5. Show All Customer Records")
        print("6. Return to Main Menu")
        print("=================================================================")
        options = int(input("Enter between 1 to 5 -------> : "))
        if options == 1:
            Customer.insertCustomer()
        elif options == 2:
            Customer.searchCustomer()
        elif options == 3:
            Customer.deleteCustomer()
        elif options == 4:
            Customer.updateCustomer()
        elif options == 5:
            Customer.showCustomerTable()
        elif options == 6:
            print('\n' * 5)
            return
        else:
            print("Wrong Choice.....Enter your options again")
            x = input("Enter any key to continue")