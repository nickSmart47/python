from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.department import Department
from flask_app.models.employee import Employee

@app.route('/') # list all departments
def index():
    all_departments = Department.get_all_departments()
    return render_template('index.html', departments = all_departments)

@app.route('/departments/create', methods=['POST'])
def create_department():
    data = {
        'name': request.form['department_name'],
        'location': request.form['department_location']
    }
    if (Department.validate_department(data) == True):
        Department.create_new_department(data)
    return redirect('/')

@app.route('/departments/<int:department_id>/delete')
def delete_department(department_id):
    data = {
        'id': department_id
    }
    Department.delete_department(data)
    return redirect('/')

@app.route('/departments/<int:department_id>/edit')
def edit_department(department_id):
    data = {
        'id': department_id
    }
    department = Department.get_single_department(data)
    return render_template('edit_department.html', department = department)

@app.route('/departments/<int:department_id>/update', methods=['POST'])
def update_department(department_id):
    data = {
        'name': request.form['department_name'],
        'location': request.form['department_location'],
        'id': department_id
    }
    if Department.validate_department(data):
        Department.update_single_department(data)
        return redirect('/')
    else:
        return redirect(f'/departments/{department_id}/edit')

@app.route('/departments/<int:department_id>')
def get_single_department(department_id):
    data = {
        'id': department_id
    }
    department = Department.get_single_department(data)
    return render_template('department.html', department = department)

@app.route("/departments/<int:department_id>/add_employee", methods = ["POST"])
def create_employee_for_department(department_id):
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'salary' : request.form['salary'],
        'department_id' : department_id
        }
    if Employee.validate_employee(data):
        Employee.create_new_employee(data)
        return redirect(f'/departments/{department_id}')

    return redirect(f'/departments/{department_id}')