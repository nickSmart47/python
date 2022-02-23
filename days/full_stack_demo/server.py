from flask import Flask, render_template, redirect
from department import Department

app = Flask(__name__)

@app.route('/') # list all departments
def index():
    departments = Department.get_all_departments()
    return render_template('index.html', departments = departments)

if __name__ == '__main__':
    app.run(debug=True)