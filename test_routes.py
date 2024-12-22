
import unittest
from app import app, db
from models import Employee

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
            email="test.user@example.com"
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
            "email": "new.user@example.com"
        }
        response = self.app.post('/employee', json=new_employee)
        self.assertEqual(response.status_code, 201)
        self.assertIn("New User", response.get_data(as_text=True))

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

    def test_refresh_database(self):
        response = self.app.post('/refresh-database')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Database refreshed successfully", response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()