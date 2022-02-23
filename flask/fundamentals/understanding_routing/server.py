from flask import Flask

app = Flask(__name__)



# Create a server file that generates the specified responses for the following url requests:

# 1. localhost:5000/ - have it say "Hello World!"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# 2. localhost:5000/dojo - have it say "Dojo!"
@app.route('/dojo')
def success():
    return "Dojo!"

# 3. Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"
@app.route('/say/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    name = str(name)
    return f"Hi {name.title()}!"

# 4. Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times


@app.route('/repeat/<number>/<word>') 
def repeat_number_of_times(number, word):
    number = int(number)
    word = str(word)
    return (word + " ") * number

@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

