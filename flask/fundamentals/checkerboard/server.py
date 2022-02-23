from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<rows>')
def variable_rows(rows):
    rows = int(rows)
    return render_template("index.html", rows=rows)

@app.route('/<rows>/<columns>')
def variable_rows_and_columns(rows, columns):
    rows = int(rows)
    columns = int(columns)
    return render_template("index.html", rows=rows, columns=columns)

@app.route('/<rows>/<columns>/<color1>/<color2>')
def variable_rows_and_columns_and_colors(rows, columns, color1, color2):
    rows = int(rows)
    columns = int(columns)
    color1, color2 = str(color1), str(color2)
    return render_template("index.html", rows=rows, columns=columns, color1=color1, color2=color2)

if __name__ =='__main__':
    app.run(debug=True)