from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # print(request.form)
    total_num_items = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    print(f"Charging {first_name} {last_name} for {total_num_items} fruits ")
    return render_template("checkout.html",
    num_strawberry = request.form['strawberry'],
    num_raspberry = request.form['raspberry'],
    num_apple = request.form['apple'],
    first_name = first_name,
    last_name = last_name,
    student_id = request.form['student_id'],
    total_num_items = total_num_items)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    