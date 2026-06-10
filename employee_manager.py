import json

FILE_NAME = "employees.json"

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []
    
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_employee():
    data = load_data()

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = input("Enter Salary: ")

    employee = {
        "id": emp_id,
        "name": name,
        "salary": salary
    }

    data.append(employee)
    save_data(data)

    print("Employee Added Successfully!")

def view_employees():
    data = load_data()

    if not data:
        print("No Records Found")
        return

    for emp in data:
        print(emp)

def update_employee():
    data = load_data()

    emp_id = input("Enter Employee ID to Update: ")

    for emp in data:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter New Name: ")
            emp["salary"] = input("Enter New Salary: ")

            save_data(data)
            print("Employee Updated!")
            return

    print("Employee Not Found")

def update_employee():
    data = load_data()

    emp_id = input("Enter Employee ID to Update: ")

    for emp in data:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter New Name: ")
            emp["salary"] = input("Enter New Salary: ")

            save_data(data)
            print("Employee Updated!")
            return

    print("Employee Not Found")

while True:
    print("\nEMPLOYEE RECORDS MANAGER")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        update_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")