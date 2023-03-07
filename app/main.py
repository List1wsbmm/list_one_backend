from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hi there! How are you today?'

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        greeting = f'Hello {name}! Have a great day!'
        return render_template('greet.html', greeting=greeting)
    else:
        return render_template('greet.html')

if __name__ == '__main__':
    app.run()
