from app import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Float, nullable=True)
    country = db.Column(db.String(100), nullable=True)
    hiring_date = db.Column(db.Date, nullable=True)
    previous_salary = db.Column(db.Float, nullable=True)
    last_promoted_date = db.Column(db.Date, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "position": self.position,
            "department": self.department,
            "email": self.email,
            "salary": self.salary,
            "country": self.country,
            "hiring_date": self.hiring_date,
            "previous_salary": self.previous_salary,
            "last_promoted_date": self.last_promoted_date
        }