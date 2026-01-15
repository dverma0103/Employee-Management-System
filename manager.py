import re
from employees import Employee
import json
import os

class EmployeeManager:
    def __init__(self, file_name = "employees.json"):
        self.file_name = file_name
        self.employees = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.file_name):
            try:
                with open(self.file_name, 'r') as file:
                    return json.load(file)
            except FileNotFoundError:
                return []
        return []
    
    def save_data(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.employees, file, indent=4)
    
    def add_employee(self, emp_id, name, age, department, salary):
        for emp in self.employees:
            if emp_id == emp["id"]:
                print("\n***** Employee Already Exist *****")
                return
        employee = Employee(emp_id, name, age, department, salary)
        self.employees.append(employee.to_dict())
        self.save_data()
        print("\n***** Employee Added Succsessfully *****")
    
    def view_employee(self):
        if not self.employees:
            print("\n***** No Entry in Employee Data *****")
            return
        for emp in self.employees:
            print(emp)
    
    def search_employee(self, emp_id):
        if not self.employees:
            print("\n***** No Entry in Employee Data *****")
        for emp in self.employees:
            if emp_id == emp["id"]:
                print(emp)
                return
        else:
            print("\n***** Employee Not Found *****")
    
    def update_employee(self, emp_id, column, new_entry):
        column = column.lower()
        if not self.employees:
            print("\n***** No Entry in Employee Data *****")
            return
        for emp in self.employees:
            if emp_id == emp["id"]:
                try:
                    emp[column] = int(new_entry)
                except:
                    emp[column] = new_entry
                self.save_data()
                return print("\n***** Employee Data Successfully Updated *****")
        else:
            print("\n***** Employee Not Found *****")
    
    def delete_employee(self, emp_id):
        if not self.employees:
            print("\n***** No Entry in Employee Data *****")
            return
        for emp in self.employees:
            if emp_id == emp["id"]:
                self.employees.remove(emp)
                self.save_data()
                return print("\n***** Employee Successfully Deleted *****")
        else:
            print("\n***** Employee Not Found *****")