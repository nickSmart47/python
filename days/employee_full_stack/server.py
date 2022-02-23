from flask import Flask, render_template, redirect, request
from department import Department

app = Flask(__name__)


@app.route('/')  # list all departments
def index():
    all_departments = Department.get_all_departments()
    return render_template('index.html', departments=all_departments)


@app.route('/departments/create', methods=['POST'])
def create_department():
    data = {
        'name': request.form['department_name'],
        'location': request.form['department_location']
    }
    Department.create_new_department(data)
    return redirect('/')


@app.route('/departments/<int:department_id>/delete')
def delete_department(department_id):
    data = {
        'id' : department_id
    }
    Department.delete_department(data)
    return redirect('/')

@app.route('/departments/<int:department_id>/edit')
def edit_department(department_id):
    data = {
        'id' : department_id
    }
    department = Department.get_single_department(data)
    return render_template('edit_department.html', department = department)

@app.route('/departments/<int:department_id>/update', methods=['POST'])
def update_department(department_id):
    data = {
        'name' : request.form['department_name'],
        'location' : request.form['department_location'],
        'id' : department_id,
    }
    Department.update_single_department(data)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)
