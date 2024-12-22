
import unittest
from app import db
from models import Employee

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_employee_creation(self):
        employee = Employee(
            name="Test User",
            position="Tester",
            department="QA",
            email="test.user@example.com"
        )
        db.session.add(employee)
        db.session.commit()
        self.assertIsNotNone(employee.id)

    def test_employee_to_dict(self):
        employee = Employee(
            name="Test User",
            position="Tester",
            department="QA",
            email="test.user@example.com"
        )
        db.session.add(employee)
        db.session.commit()
        employee_dict = employee.to_dict()
        self.assertEqual(employee_dict['name'], "Test User")
        self.assertEqual(employee_dict['position'], "Tester")
        self.assertEqual(employee_dict['department'], "QA")
        self.assertEqual(employee_dict['email'], "test.user@example.com")

if __name__ == '__main__':
    unittest.main()