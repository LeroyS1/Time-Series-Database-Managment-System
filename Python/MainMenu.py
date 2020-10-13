import SubMenu

while True:
     print("Welcome to our SuperMarket Database\n")
     print("Please choose one of the following options: \n")
     print("=====================================================================")
     print("1. Sales")
     print("2. Product Management")
     print("3. Employee Management")
     print("4. Customer Management")
     print("5. Exit")
     print("=====================================================================")
     options = int(input("Enter between 1 to 5 -------> : "))
     if options == 1:
          EmployeeID = int(input("Please enter EmployeeID: "))
          print('\n' * 5)
          SubMenu.MenuSales(EmployeeID)
     elif options == 2:
          print('\n' * 5)
          SubMenu.MenuItemInfo()
     elif options == 3:
          print('\n' * 5)
          SubMenu.MenuEmployee()
     elif options == 4:
          print('\n' * 5)
          SubMenu.MenuCustomer()
     elif options == 5:
          break
     else:
          print("Wrong Choice.....Enter Your Choice again")
          x = input("Press any key to continue: ") 