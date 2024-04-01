from flask import Flask, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return '''
        <form action="/guess" method="post">
            <label for="number">Guess a number between 0-9:</label>
            <input type="number" id="number" name="number" min="0" max="9">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route("/guess", methods=["POST"])
def guess():
    user_chosen_number = int(request.form['number'])
    number_randomly_chosen = random.randint(0, 9)
    result = "correct" if user_chosen_number == number_randomly_chosen else "incorrect"
    return f'''
        <h1>Your guess is {result}!</h1>
        <p>You chose {user_chosen_number}, and the server chose {number_randomly_chosen}.</p>
        <img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW9xc3NoM2NjN3hxMzAzd20wd29pc3BtNzc1cmN6dDJtZGxjNTQxayZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PK1YQhAoBOpP2/200.webp' width='400'>
    '''

if __name__ == "__main__":
    app.run(debug=True)  # Can toggle this: True or False, depending on your needs
