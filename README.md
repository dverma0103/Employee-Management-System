# Employee Management System (Python CLI)

A menu-driven Python command-line application to manage employee records.  
The system allows users to perform basic CRUD (Create, Read, Update, Delete) operations with persistent data storage using a JSON file.

This project is built to strengthen core Python fundamentals and demonstrate clean, modular coding practices.

---

## 🚀 Features
- Add new employee records
- View all employees
- Search employee by ID
- Update employee details
- Delete employee records
- Persistent data storage using JSON file

---

## 🧠 Concepts & Skills Used
- Python functions
- Lists and dictionaries
- Conditional statements and loops
- Menu-driven program design
- File handling using JSON
- Basic CRUD operations
- Git & GitHub for version control

---

## 📂 Project Structure
Employee-Management-System/
│
├── employee_management.py # Main Python application
├── employees.json # JSON file for persistent storage
└── README.md # Project documentation


---

## ⚙️ Application Flow
1. The program loads existing employee data from `employees.json` at startup
2. The user selects an option from the menu
3. The selected operation is performed on the employee data
4. Any changes are saved back to the JSON file
5. Data remains available even after the program exits

---

## ▶️ How to Run the Project

### Prerequisites
- Python 3.x installed on your system

### Steps to Run
```bash
git clone https://github.com/dverma0103/Employee-Management-System.git
cd Employee-Management-System
python employee_management.py

1. Add Employee
2. View All Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit

🔮 Future Enhancements

Add exception handling for invalid user inputs

Refactor the code using Object-Oriented Programming (OOP)

Store employee data in CSV or database

Convert the application into a REST API using FastAPI

📌 Purpose of This Project

This project simulates a simple real-world employee management system and helps build strong fundamentals required for backend development, data handling, and future AI/ML pipelines.

👨‍💻 Author

Deepak Verma
GitHub: https://github.com/dverma0103