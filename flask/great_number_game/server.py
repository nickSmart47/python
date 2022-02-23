from flask import Flask, render_template, redirect, session, request
from random import randint

app = Flask(__name__)
app.secret_key = 'this game is hard'




@app.route('/')
def index():
    session['answer'] = randint(1, 100)
    answer = session['answer']
    print(f"Pssst, the answer is: {answer}")
    return render_template('index.html')

@app.route('/guess', methods = ["POST"])
def guess():
    answer = session['answer']
    user_guess = int(request.form['guess'])
    print(f"User guess is {user_guess}")
    print(f"Answer is: {answer}")
    if user_guess == answer:
        user_wins = f"You guessed it! The answer was {answer}"
        session.clear()
        return render_template('guess.html', user_wins = user_wins)
    elif user_guess > answer:
        too_high = "Too High!"
        return render_template('guess.html', too_high = too_high)
    elif user_guess < answer:
        too_low = "Too Low!"
        return render_template('guess.html', too_low = too_low)
    return render_template('guess.html')

if __name__ == '__main__':
    app.run(debug=True)
