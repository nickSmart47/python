from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('hello')
    return 'Welcome 2 my webbed site :3'

@app.route('/hamburger')
def hamburger():
    return 'I like a good burger!'

@app.route('/multiply/<int:x>/<int:y>')
def multiply_two_numbers(x,y): # parameters need to match what's inside the route
    # new_x = int(x)
    # new_y = int(y)
    # return f'The result of {new_x} and {new_y} is {new_x * new_y}'
    return f'The result of {x} and {y} is {x * y}'

if __name__ == '__main__':
    app.run(debug=True)