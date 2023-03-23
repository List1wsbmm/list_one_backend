"""
This module contains the main Flask application.
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """
    Display a simple greeting message.
    """
    return 'Hi there! How are you today?'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    """
    Display a greeting message based on user input.
    """
    if request.method == 'POST':
        name = request.form['name']
        greeting = f'Hello {name}! Have a great day!'
        return render_template('greet.html', greeting=greeting)
    return render_template('greet.html')

if __name__ == '__main__':
    app.run()
