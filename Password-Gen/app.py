from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)

def generate_password(length, include_numbers=False, include_symbols=False):
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password')
def get_password():
    length = int(request.args.get('length'))
    include_numbers = request.args.get('include_numbers') == 'true'
    include_symbols = request.args.get('include_symbols') == 'true'
    
    password = generate_password(length, include_numbers, include_symbols)
    return render_template('password.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
