# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us at sindhuilango2000@gmail.com'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
