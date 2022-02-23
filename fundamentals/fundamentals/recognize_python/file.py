# Variable Declarations start
num1 = 42
num2 = 2.3
boolean = True
string = 'Hello World'
# pizza toppings is a list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# person is a dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# fruit is a tuple
fruit = ('blueberry', 'strawberry', 'banana')
# Variable declarations end

# print is log statemen
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

# if and else are conditional statements
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")


# for loop start
for x in range(5):
    print(x)
# for loop stop
# for loop start
for x in range(2,5):
    print(x)
# for loop stop
# for loop start
for x in range(2,10,3):
    print(x)
# for loop stop
x = 0
# while loop start
while(x < 5):
    print(x)
    x += 1 # increment
# while loop stop

# .pop removes last value from a list
pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color') # removes eye color from person dictionary
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue # continues loop if this condition is met
    print('After 1st if statement')
    if topping == 'Olives':
        break # breaks out of loop if this condition is met

# function declaration
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

# function declaration that takes in one parameter as argument
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)