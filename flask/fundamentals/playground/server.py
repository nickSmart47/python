from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Playground Assignment!"

@app.route('/play')
def play():
    return render_template("play.html")

@app.route('/play/<number>')
def play_number(number):
    number = int(number)
    return render_template("play.html", number=number)

@app.route('/play/<number>/<color>')
def play_number_wtih_color(number,color):
    number = int(number)
    color = str(color)
    return render_template("play.html", number=number, color=color)

if __name__ == '__main__':
    app.run(debug=True)