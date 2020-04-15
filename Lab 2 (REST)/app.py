from flask import Flask, jsonify, request, Response
from EmployeeModel import *
from settings import *
import json


# Read operation
@app.route('/employees')
def get_employee():
    return jsonify({'employees': Employee.get_all_employees()})

# get employee by id
@app.route ('/employees/<int:id>')
def get_employee_by_id(id):
    return_value = Employee.get_employee(id)
    return jsonify(return_value)

# Validation
def valid_employee_object(employee_object):
	if ("id" in employee_object and "name" in employee_object and "salary" in employee_object):
		return True
	else:
		return False

def valid_put_request_data(request_data):
	if("name" in request_data and "salary" in request_data):
		return True
	else:
		return False

def valid_patch_request_data(request_data):
	if("name" in request_data or "salary" in request_data):
		return True
	else:
		return False

# Create operation 
@app.route('/employees', methods=['POST'])
def add_employee():
    request_data = request.get_json()
    if(valid_employee_object(request_data)):
        Employee.add_employee(request_data['id'], request_data['name'], request_data['salary'])
        response = Response("", status=201, mimetype='application/json')
        response.headers['Location'] = "/employees/" + str(request_data['id'])
        return response
    else: 
        invalidEmployeeObjectErrorMsg = {
            "error": "Invalid employee object was passed in",
            "helpString": "Data should be in the following format {'id': 'employee_id', 'name': 'employee_name', 'salary': 'employee_salary'}"
        }
        response = Response(json.dumps(invalidEmployeeObjectErrorMsg), status=400, mimetype='application/json')

    if("name" in request_data):
        Employee.update_employee_name(id, request_data['name'])
    if("salary" in request_data):
        Employee.update_employee_salary(id, request_data['salary'])

    response = Response("", status=204)
    response.headers['Location'] = "/employees/" + str(id)
    return response

# Update operation
@app.route('/employees/<int:id>', methods=['PUT'])
def replace_employee(id):
    request_data = request.get_json()
    if(not valid_put_request_data(request_data)):
        invalidEmployeeObjectErrorMsg = {
            "error": "Invalid employee object was passed in",
            "helpString": "Data should be in the following format {'id': 'employee_id', 'name': 'employee_name', 'salary': 'employee_salary'}"
        }
        response = Response(json.dumps(invalidEmployeeObjectErrorMsg), status=400, mimetype='application/json')
        return response 

    Employee.replace_employee(id, request_data['name'], request_data['salary'])
    response = Response("", status=204)
    return response 


@app.route('/employees/<int:id>', methods=['PATCH'])
def update_employee(id):
    request_data = request.get_json()
    if(not valid_patch_request_data(request_data)):
        invalidEmployeeObjectErrorMsg = {
            "error": "Invalid employee object was passed in",
            "helpString": "Data should be in the following format {'id': 'employee_id', 'name': 'employee_name', 'salary': 'employee_salary'}"
        }
        response = Response(json.dumps(invalidEmployeeObjectErrorMsg), status=400, mimetype='application/json')
        return response 

    if("name" in request_data):
        Employee.update_employee_name(id, request_data['name'])
    if("salary" in request_data):
        Employee.update_employee_salary(id, request_data['salary'])

    response = Response("", status=204)
    response.headers['Location'] = "/employees" + str(id)
    return response 



# Delete Operation
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    if (Employee.delete_employee(id)): 
        response = Response("", status=204)
        return response
    invalidEmployeeObjectErrorMsg = {
        "error": "No employee with the provided id found therefore we can't delete, plase check the id "
    }
    respone = Response(json.dumps(invalidEmployeeObjectErrorMsg), status=404, mimetype='application/json')


app.run(port=5000, debug=True, host='0.0.0.0')