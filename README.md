# Employee Management System (OOPS + JSON | Python)

A menu-driven **Employee Management System** built using **Object-Oriented Programming (OOPS)** principles in Python with **JSON-based file storage**.  
This application allows users to perform CRUD operations on employee records while ensuring data persistence.

---

## 🚀 Features
- Add new employee records
- View all employees
- Search employee by ID
- Delete employee records
- Persistent data storage using JSON
- Modular and maintainable OOPS-based design

---

## 🧠 Concepts & Skills Used
- Object-Oriented Programming (Classes & Objects)
- Encapsulation and modular design
- File handling with JSON
- CRUD operations
- Separation of concerns
- Python standard libraries
- Git & GitHub version control

---

## 📂 Project Structure
employee_management/
│
├── employee.py # Employee class (data model)
├── manager.py # EmployeeManager class (business logic + file handling)
├── employees.json # JSON file for data persistence
├── main.py # Application entry point (menu-driven UI)
└── README.md # Project documentation


---

## ⚙️ How the Application Works
1. On startup, employee data is loaded from `employees.json`
2. User selects an operation from the menu
3. The selected CRUD operation is executed
4. Changes are saved back to the JSON file
5. Data persists even after program exit

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.x installed

### Steps
```bash
git clone https://github.com/dverma0103/Employee-Management-System.git
python main.py
```
### 🧪 Sample Menu

1. Add Employee
2. View All Employees
3. Search Employee
4. Delete Employee
5. Exit