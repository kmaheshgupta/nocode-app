import unittest
from app import app, db
from models import Employee
from datetime import datetime

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

        # Add a sample employee
        self.sample_employee = Employee(
            name="Test User",
            position="Tester",
            department="QA",
            email="test.user@example.com",
            salary=50000,
            country="USA",
            hiring_date=datetime.strptime("2020-01-01", '%Y-%m-%d').date(),
            previous_salary=45000,
            last_promoted_date=datetime.strptime("2021-01-01", '%Y-%m-%d').date()
        )
        db.session.add(self.sample_employee)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_employees(self):
        response = self.app.get('/employees')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test User", response.get_data(as_text=True))

    def test_get_employee(self):
        response = self.app.get(f'/employee/{self.sample_employee.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test User", response.get_data(as_text=True))

    def test_get_employee_not_found(self):
        response = self.app.get('/employee/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Employee not found", response.get_data(as_text=True))

    def test_add_employee(self):
        new_employee = {
            "name": "New User",
            "position": "Developer",
            "department": "Development",
            "email": "new.user@example.com",
            "salary": 60000,
            "country": "Canada",
            "hiring_date": "2021-01-01",
            "previous_salary": 55000,
            "last_promoted_date": "2022-01-01"
        }
        response = self.app.post('/employee', json=new_employee)
        self.assertEqual(response.status_code, 201)
        self.assertIn("New User", response.get_data(as_text=True))

    def test_add_employee_missing_fields(self):
        new_employee = {
            "name": "New User",
            "position": "Developer"
        }
        response = self.app.post('/employee', json=new_employee)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing required field: department", response.get_data(as_text=True))

    def test_update_employee(self):
        updated_data = {"name": "Updated User"}
        response = self.app.put(f'/employee/{self.sample_employee.id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated User", response.get_data(as_text=True))

    def test_update_employee_not_found(self):
        updated_data = {"name": "Updated User"}
        response = self.app.put('/employee/999', json=updated_data)
        self.assertEqual(response.status_code, 404)
        self.assertIn("Employee not found", response.get_data(as_text=True))

    def test_delete_employee(self):
        response = self.app.delete(f'/employee/{self.sample_employee.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Employee deleted", response.get_data(as_text=True))

    def test_delete_employee_not_found(self):
        response = self.app.delete('/employee/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn("Employee not found", response.get_data(as_text=True))

    def test_reset_database(self):
        response = self.app.post('/reset-database')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Database reset successfully", response.get_data(as_text=True))

    def test_chat_endpoint(self):
        response = self.app.post('/chat', json={"message": "Hello"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Did you ask about Hello?", response.get_data(as_text=True))

    def test_chat_endpoint_no_message(self):
        response = self.app.post('/chat', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("No message provided", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()