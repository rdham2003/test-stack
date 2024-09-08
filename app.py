from flask import Flask, jsonify, send_from_directory, request, session
from flask_cors import CORS
from backend.functions import cardIsValid

app = Flask(__name__, static_folder='frontend/dist', static_url_path='/')

CORS(app)

isValid = False
validator = False

@app.route('/')
def main():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data')
def get_data():
    print(isValid)
    data = {
        'isValid': isValid,
        'validator': validator
    }
    return jsonify(data)

@app.route('/check', methods=["GET", "POST"])
def ccvalidator():
    ccnum = request.form.get("ccnumber")
    
    global isValid
    global validator
    
    isValid = cardIsValid(ccnum)
    validator = True
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)