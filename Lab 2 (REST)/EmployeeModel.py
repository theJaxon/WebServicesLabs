from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import json 
from settings import app 

db = SQLAlchemy(app)

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)

    def json(self):
        return {'id': self.id, 'name': self.name, 'salary': self.salary}
    
    
    def add_employee(_id, _name, _salary):
        new_employee = Employee(id=_id, name=_name, salary=_salary)
        db.session.add(new_employee)
        db.session.commit()

    def get_employee(_id):
        return Employee.json(Employee.query.filter_by(id=_id).first())

    def get_all_employees():
        return [Employee.json(employee) for employee in Employee.query.all()]

    def delete_employee(_id):
        is_successful = Employee.query.filter_by(id=_id).delete()
        db.session.commit()
        return bool(is_successful)

    def update_employee_name(_id, _name):
        employee_to_update = Employee.query.filter_by(id=_id).first()
        employee_to_update.name = _name 
        db.session.commit()

    def update_employee_salary(_id, _salary):
        employee_to_update = Employee.query.filter_by(id=_id).first()
        employee_to_update.salary = _salary
        db.session.commit()

    def replace_employee(_id, _name, _salary):
        employee_to_replace = Employee.query.filter_by(id=_id).first()
        employee_to_replace.name = _name 
        employee_to_replace.salary = _salary
        db.session.commit()


    def __repr__(self):
        employee_object = {
            'id': self.id, 
            'name': self.name,
            'salary': self.salary

        }
        return json.dumps(employee_object)