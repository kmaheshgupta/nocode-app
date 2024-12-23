from flask import jsonify, request
from app import app, db
from models import Employee
from datetime import datetime

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])

@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get(id)
    if employee:
        return jsonify(employee.to_dict())
    return jsonify({"error": "Employee not found"}), 404

@app.route('/employee', methods=['POST'])
def add_employee():
    data = request.json
    required_fields = ['name', 'position', 'department', 'email']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    new_employee = Employee(
        name=data['name'],
        position=data['position'],
        department=data['department'],
        email=data['email'],
        salary=data.get('salary'),
        country=data.get('country'),
        hiring_date=datetime.strptime(data.get('hiring_date'), '%Y-%m-%d').date() if data.get('hiring_date') else None,
        previous_salary=data.get('previous_salary'),
        last_promoted_date=datetime.strptime(data.get('last_promoted_date'), '%Y-%m-%d').date() if data.get('last_promoted_date') else None
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.to_dict()), 201

@app.route('/employee/<id>', methods=['PUT'])
def update_employee(id):
    employee = Employee.query.get(id)
    if employee:
        employee.name = request.json.get('name', employee.name)
        employee.position = request.json.get('position', employee.position)
        employee.department = request.json.get('department', employee.department)
        employee.email = request.json.get('email', employee.email)
        employee.salary = request.json.get('salary', employee.salary)
        employee.country = request.json.get('country', employee.country)
        employee.hiring_date = datetime.strptime(request.json.get('hiring_date'), '%Y-%m-%d').date() if request.json.get('hiring_date') else employee.hiring_date
        employee.previous_salary = request.json.get('previous_salary', employee.previous_salary)
        employee.last_promoted_date = datetime.strptime(request.json.get('last_promoted_date'), '%Y-%m-%d').date() if request.json.get('last_promoted_date') else employee.last_promoted_date
        db.session.commit()
        return jsonify(employee.to_dict())
    return jsonify({"error": "Employee not found"}), 404

@app.route('/employee/<id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get(id)
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return jsonify({"message": "Employee deleted"}), 200
    return jsonify({"error": "Employee not found"}), 404

@app.route('/reset-database', methods=['POST'])
def reset_database():
    try:
        db.drop_all()
        db.create_all()
        load_initial_data()
        return jsonify({"message": "Database reset successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        response_message = f"Did you ask about {user_message}?"
        return jsonify({"response": response_message}), 200
    return jsonify({"error": "No message provided"}), 400

def load_initial_data():
    if Employee.query.count() == 0:
        initial_employees = [
            {"name": "John Doe", "position": "Software Engineer", "department": "Development", "email": "john.doe@example.com", "salary": 60000, "country": "USA", "hiring_date": "2020-01-15", "previous_salary": 55000, "last_promoted_date": "2021-06-01"},
            {"name": "Jane Smith", "position": "Project Manager", "department": "Management", "email": "jane.smith@example.com", "salary": 80000, "country": "Canada", "hiring_date": "2019-03-22", "previous_salary": 75000, "last_promoted_date": "2020-12-15"},
            {"name": "Emily Johnson", "position": "HR Specialist", "department": "Human Resources", "email": "emily.johnson@example.com", "salary": 50000, "country": "UK", "hiring_date": "2018-07-30", "previous_salary": 45000, "last_promoted_date": "2019-11-20"},
            {"name": "Michael Brown", "position": "Data Analyst", "department": "Analytics", "email": "michael.brown@example.com", "salary": 70000, "country": "Australia", "hiring_date": "2021-05-10", "previous_salary": 65000, "last_promoted_date": "2022-01-25"},
            {"name": "Linda Davis", "position": "Marketing Coordinator", "department": "Marketing", "email": "linda.davis@example.com", "salary": 55000, "country": "Germany", "hiring_date": "2017-09-18", "previous_salary": 50000, "last_promoted_date": "2018-08-05"},
            {"name": "James Wilson", "position": "Customer Support", "department": "Support", "email": "james.wilson@example.com", "salary": 45000, "country": "France", "hiring_date": "2020-11-12", "previous_salary": 40000, "last_promoted_date": "2021-07-30"},
            {"name": "Patricia Martinez", "position": "Software Engineer", "department": "Development", "email": "patricia.martinez@example.com", "salary": 62000, "country": "Spain", "hiring_date": "2019-02-25", "previous_salary": 57000, "last_promoted_date": "2020-09-10"},
            {"name": "Robert Anderson", "position": "Project Manager", "department": "Management", "email": "robert.anderson@example.com", "salary": 82000, "country": "Italy", "hiring_date": "2018-06-14", "previous_salary": 77000, "last_promoted_date": "2019-12-01"},
            {"name": "Mary Thomas", "position": "HR Specialist", "department": "Human Resources", "email": "mary.thomas@example.com", "salary": 52000, "country": "Netherlands", "hiring_date": "2017-10-05", "previous_salary": 47000, "last_promoted_date": "2018-11-15"},
            {"name": "William Jackson", "position": "Data Analyst", "department": "Analytics", "email": "william.jackson@example.com", "salary": 72000, "country": "Sweden", "hiring_date": "2021-04-20", "previous_salary": 67000, "last_promoted_date": "2022-02-10"},
            {"name": "Barbara White", "position": "Marketing Coordinator", "department": "Marketing", "email": "barbara.white@example.com", "salary": 56000, "country": "Norway", "hiring_date": "2016-08-25", "previous_salary": 51000, "last_promoted_date": "2017-07-15"},
            {"name": "David Harris", "position": "Customer Support", "department": "Support", "email": "david.harris@example.com", "salary": 46000, "country": "Denmark", "hiring_date": "2019-12-10", "previous_salary": 41000, "last_promoted_date": "2020-08-20"},
            {"name": "Jennifer Clark", "position": "Software Engineer", "department": "Development", "email": "jennifer.clark@example.com", "salary": 64000, "country": "Finland", "hiring_date": "2018-03-15", "previous_salary": 59000, "last_promoted_date": "2019-10-05"},
            {"name": "Charles Lewis", "position": "Project Manager", "department": "Management", "email": "charles.lewis@example.com", "salary": 84000, "country": "Switzerland", "hiring_date": "2017-05-22", "previous_salary": 79000, "last_promoted_date": "2018-12-10"},
            {"name": "Elizabeth Walker", "position": "HR Specialist", "department": "Human Resources", "email": "elizabeth.walker@example.com", "salary": 54000, "country": "Belgium", "hiring_date": "2016-09-30", "previous_salary": 49000, "last_promoted_date": "2017-11-20"},
            {"name": "Joseph Hall", "position": "Data Analyst", "department": "Analytics", "email": "joseph.hall@example.com", "salary": 74000, "country": "Austria", "hiring_date": "2020-02-18", "previous_salary": 69000, "last_promoted_date": "2021-01-15"},
            {"name": "Susan Allen", "position": "Marketing Coordinator", "department": "Marketing", "email": "susan.allen@example.com", "salary": 57000, "country": "Ireland", "hiring_date": "2015-07-10", "previous_salary": 52000, "last_promoted_date": "2016-06-25"},
            {"name": "Thomas Young", "position": "Customer Support", "department": "Support", "email": "thomas.young@example.com", "salary": 47000, "country": "Portugal", "hiring_date": "2018-11-05", "previous_salary": 42000, "last_promoted_date": "2019-09-15"},
            {"name": "Jessica King", "position": "Software Engineer", "department": "Development", "email": "jessica.king@example.com", "salary": 66000, "country": "Poland", "hiring_date": "2017-01-20", "previous_salary": 61000, "last_promoted_date": "2018-08-10"},
            {"name": "Christopher Wright", "position": "Project Manager", "department": "Management", "email": "christopher.wright@example.com", "salary": 86000, "country": "Czech Republic", "hiring_date": "2016-04-15", "previous_salary": 81000, "last_promoted_date": "2017-11-05"}
        ]
        for emp_data in initial_employees:
            emp_data['hiring_date'] = datetime.strptime(emp_data['hiring_date'], '%Y-%m-%d').date() if emp_data.get('hiring_date') else None
            emp_data['last_promoted_date'] = datetime.strptime(emp_data['last_promoted_date'], '%Y-%m-%d').date() if emp_data.get('last_promoted_date') else None
            new_employee = Employee(**emp_data)
            db.session.add(new_employee)
        db.session.commit()