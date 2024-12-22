from flask import jsonify, request
from app import app, db
from models import Employee

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
    new_employee = Employee(
        name=data['name'],
        position=data['position'],
        department=data['department'],
        email=data['email']
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

@app.route('/refresh-database', methods=['POST'])
def refresh_database():
    try:
        db.drop_all()
        db.create_all()
        load_initial_data()
        return jsonify({"message": "Database refreshed successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def load_initial_data():
    if Employee.query.count() == 0:
        initial_employees = [
            {"name": "John Doe", "position": "Software Engineer", "department": "Development", "email": "john.doe@example.com"},
            {"name": "Jane Smith", "position": "Project Manager", "department": "Management", "email": "jane.smith@example.com"},
            {"name": "Emily Johnson", "position": "HR Specialist", "department": "Human Resources", "email": "emily.johnson@example.com"},
            {"name": "Michael Brown", "position": "Data Analyst", "department": "Analytics", "email": "michael.brown@example.com"},
            {"name": "Linda Davis", "position": "Marketing Coordinator", "department": "Marketing", "email": "linda.davis@example.com"},
            {"name": "James Wilson", "position": "Customer Support", "department": "Support", "email": "james.wilson@example.com"},
            {"name": "Patricia Martinez", "position": "Software Engineer", "department": "Development", "email": "patricia.martinez@example.com"},
            {"name": "Robert Anderson", "position": "Project Manager", "department": "Management", "email": "robert.anderson@example.com"},
            {"name": "Mary Thomas", "position": "HR Specialist", "department": "Human Resources", "email": "mary.thomas@example.com"},
            {"name": "William Jackson", "position": "Data Analyst", "department": "Analytics", "email": "william.jackson@example.com"},
            {"name": "Barbara White", "position": "Marketing Coordinator", "department": "Marketing", "email": "barbara.white@example.com"},
            {"name": "David Harris", "position": "Customer Support", "department": "Support", "email": "david.harris@example.com"},
            {"name": "Jennifer Clark", "position": "Software Engineer", "department": "Development", "email": "jennifer.clark@example.com"},
            {"name": "Charles Lewis", "position": "Project Manager", "department": "Management", "email": "charles.lewis@example.com"},
            {"name": "Elizabeth Walker", "position": "HR Specialist", "department": "Human Resources", "email": "elizabeth.walker@example.com"},
            {"name": "Joseph Hall", "position": "Data Analyst", "department": "Analytics", "email": "joseph.hall@example.com"},
            {"name": "Susan Allen", "position": "Marketing Coordinator", "department": "Marketing", "email": "susan.allen@example.com"},
            {"name": "Thomas Young", "position": "Customer Support", "department": "Support", "email": "thomas.young@example.com"},
            {"name": "Jessica King", "position": "Software Engineer", "department": "Development", "email": "jessica.king@example.com"},
            {"name": "Christopher Wright", "position": "Project Manager", "department": "Management", "email": "christopher.wright@example.com"}
        ]
        for emp_data in initial_employees:
            new_employee = Employee(**emp_data)
            db.session.add(new_employee)
        db.session.commit()