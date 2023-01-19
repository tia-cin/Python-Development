from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h2>Hello World</h2>'

app.run()

# COMMANDS
# python -m venv new-env
# source new-env/Scripts/activate
# pip install flask

# FLASK_APP=flask.py flask run
# FLASK_ENV=development
# flask run
