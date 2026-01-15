from manager import EmployeeManager

def menu():
    print("\nWelcome to Employee Data Management System\n")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

mngr = EmployeeManager()

while True:
    menu()
    choice = input("\nChoose an option: ")
    
    if choice == "1":
        emp_id = int(input("Enter Employee Id: "))
        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Department: ")
        salary = int(input("Enter Employee Salary: "))
        mngr.add_employee(emp_id, name, age, department, salary)
    elif choice == "2":
        mngr.view_employee()
    elif choice == "3":
        emp_id = int(input("\nEnter Employee ID: "))
        mngr.search_employee(emp_id)
    elif choice == "4":
        emp_id = int(input("Enter Employee ID: "))
        column = input("What do you want to change (Name/Age/Department/Salary): ")
        new_entry = input("Enter Updated Entry: ")
        mngr.update_employee(emp_id, column, new_entry)
    elif choice == "5":
        emp_id = int(input("Enter Employee ID: "))
        mngr.delete_employee(emp_id)
    elif choice == "6":
        print("\n***** Exiting *****")
        break
    else:
        print("\n***** Invalid Choice *****")