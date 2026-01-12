employees = []

def menu():
    print("Enter option from below: ")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit\n")

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    for emp in employees:
        if emp_id == emp['id']:
            return print("\nEmployee ID already exist.\n")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")

    employee = {
        "id": emp_id,
        "name": name,
        "age": age,
        "department": department
    }

    employees.append(employee)
    print("\nEmployee Added Sucessfully\n")

def view_employee():
    if not employees:
        print("No Employees Find...\n")
        return
    for emp in employees:
        print(f"\nID: {emp['id']}\nName: {emp['name']}\nAge: {emp['age']}\nDepartment: {emp['department']}\n")

def search_employee():
    if not employees:
        return print("\nNo Employee Data Available\n")
    emp_id = int(input("Enter Employee ID: "))
    for emp in employees:
        if emp_id == emp['id']:
            print(f"\n{emp}\n")
            break
    else:
        print("\nEmployee Details Not Present\n")
        
def update_id():
    if not employees:
        return print("\nNo Employee Data Available\n")
    emp_id = int(input("Enter Employee ID: "))
    for emp in employees:
        if emp_id == emp['id']:
            new_id = int(input("Enter New Employee ID: "))
            if new_id == emp['id']:
                return print("\nEmployee ID already exist.")
            else:
                emp['id'] = new_id
                print("\nChanges Made Sucessfully\n")
                break
    else:
        print("Error")

def update_name():
    if not employees:
        return print("\nNo Employee Data Available\n")
    emp_id = int(input("Enter Employee ID: "))
    for emp in employees:
        if emp_id == emp['id']:
            name = input("Enter New Employee Name: ")
            emp['name'] = name
            print("\nChanges Made Sucessfully\n")
            break
    else:
        print("Error")

def update_department():
    if not employees:
        return print("\nNo Employee Data Available\n")
    emp_id = int(input("Enter Employee ID: "))
    for emp in employees:
        if emp_id == emp['id']:
            dept = input("Enter New Employee Department: ")
            emp['department'] = dept
            print("\nChanges Made Sucessfully\n")
            break
    else:
        print("Error")

def update_age():
    if not employees:
        return print("\nNo Employee Data Available\n")
    emp_id = int(input("Enter Employee ID: "))
    for emp in employees:
        if emp_id == emp['id']:
            age = int(input("Enter New Employee Age: "))
            emp['age'] = age
            print("\nChanges Made Sucessfully\n")
            break
    else:
        print("Error")


def update_item():
    change = input("What you want to update ID/Name/Department/Age: ")
    change = change.lower()
    if change == "id":
        update_id()
    elif change == "name":
        update_name()
    elif change == "department":
        update_department()
    elif change == "age":
        update_age()
    else:
        print("\nPlease make a valid choice.\n")

def delete_item():
    if not employees:
        return print("\nNo Employee Data Available\n")
    emp_id = int(input("Enter Employee ID: "))
    for emp in employees:
        if emp_id == emp['id']:
            employees.remove(emp)
            print("\nEmployee details deleted sucessfully.")
            return
    print("Employee not found.")

while True:
    menu()
    choice = input("Enter a number:")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employee()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_item()
    elif choice == "5":
        delete_item()
    elif choice == "6":
        print("Exiting Program....")
        break
    else:
        print("Invalid Choice")