# 1. Import Flask
from flask import Flask, jsonify

# 2. Create an app

app = Flask(__name__)
# 3. Define index route
@app.route('/')
def index():
    return "Hello, world!"

# 4. Define the about route
@app.route('/about')
def about():
    name = 'Peleke'
    location = 'Tien Shan'

# 5. Define the contact route
@app.route('/contact')
def contact():
    email = 'peleke@example.com'
    
    return f'Questions? Comments? Complains? Shoot an email to {email}.'

# 6. Define main behavior

if __name__ == "__main__":
    app.run(debut=True)

if __name__ == "__main__":
    app.run(debug=True)
