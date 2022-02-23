class Employee():

    all_employees = []

    def __init__(self, f_name, l_name, m_name=None):
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name
        self.salary = 40000
        Employee.all_employees.append(self)

    def full_name(self):
        if self.middle_name is not None:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    def set_salary(self, new_salary):
        try:
            new_cast_salary = int(new_salary)
            if new_cast_salary < 40000:
                pass
            else:
                self.salary = new_cast_salary
        except:
            pass

    @classmethod
    def give_percentage_raise(cls, percent):
        for employee in cls.all_employees:
            employee.set_salary(employee.salary * percent)

    def __repr__(self):
        return f"{self.first_name[0]}. {self.last_name} - {self.salary}"

    # def __str__(self):
    #     return f"{self.first_name[0]}. {self.last_name} - {self.salary}"

new_employee_1 = Employee('Mark', 'Adams', 'Anthony')
new_employee_2 = Employee('Sarah', 'Smith', 'Elizabeth')
new_employee_3 = Employee(f_name='Adam', m_name='Bart', l_name='Jones')
new_employee_4 = Employee('Melissa', 'Hart-Smart')

# employees = [new_employee_1, new_employee_2, new_employee_3, new_employee_4]

# for employee in employees:
#     employee.set_salary(employee.salary * 1.1)

new_employee_1.set_salary(60000)
new_employee_2.set_salary(new_employee_2.salary * 1.05)
new_employee_3.set_salary("72000")
new_employee_4.set_salary("fifty five thousand")

Employee.give_percentage_raise(1.05)

for employee in Employee.all_employees:
    # print(f"{employee.full_name()} - Salary: {employee.salary}")
    print(employee)
