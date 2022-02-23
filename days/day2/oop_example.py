first_employee = {'first_name': 'Mike', 'last_name': 'Lawson', 'salary': 78000}
second_employee = {'first_name': 'Sarah', 'last_name': 'Michaels', 'salary': 91000}
third_employee = {'first_name': 'Adam', 'last_name': 'Jones', 'salary': 53000}

employees = [first_employee, second_employee, third_employee]

# for employee in employees:
#     print(employee['first_name']) # only works if all keys have same name

for employee in employees:
    employee['salary'] *= 1.1
    print(employee['salary'])