import unittest
from app import db
from models import Employee
from datetime import datetime

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
            email="test.user@example.com",
            salary=50000,
            country="USA",
            hiring_date=datetime.strptime("2020-01-01", '%Y-%m-%d').date(),
            previous_salary=45000,
            last_promoted_date=datetime.strptime("2021-01-01", '%Y-%m-%d').date()
        )
        db.session.add(employee)
        db.session.commit()
        self.assertIsNotNone(employee.id)

    def test_employee_creation_missing_email(self):
        with self.assertRaises(Exception):
            employee = Employee(
                name="Test User",
                position="Tester",
                department="QA"
            )
            db.session.add(employee)
            db.session.commit()

    def test_employee_to_dict(self):
        employee = Employee(
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
        db.session.add(employee)
        db.session.commit()
        employee_dict = employee.to_dict()
        self.assertEqual(employee_dict['name'], "Test User")
        self.assertEqual(employee_dict['position'], "Tester")
        self.assertEqual(employee_dict['department'], "QA")
        self.assertEqual(employee_dict['email'], "test.user@example.com")
        self.assertEqual(employee_dict['salary'], 50000)
        self.assertEqual(employee_dict['country'], "USA")
        self.assertEqual(employee_dict['hiring_date'], datetime.strptime("2020-01-01", '%Y-%m-%d').date())
        self.assertEqual(employee_dict['previous_salary'], 45000)
        self.assertEqual(employee_dict['last_promoted_date'], datetime.strptime("2021-01-01", '%Y-%m-%d').date())

if __name__ == '__main__':
    unittest.main()