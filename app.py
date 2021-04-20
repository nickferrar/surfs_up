from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    helloWorld = "Hello World!"
    for letter in helloWorld:
        print(letter)
    return 'Hello World'
