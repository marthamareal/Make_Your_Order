from flask import Flask, render_template
import pymysql

# MySQL Configurations

app = Flask(__name__)
db = pymysql.connect("localhost", "root", "F0226@vak", "OrderMeal")


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/meal')
def meal():
    return render_template('meal.html')


if __name__ == '__main__':
    app.run()
