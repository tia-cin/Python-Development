from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello():
    return '<h2>Hello World</h2>'

app.run()