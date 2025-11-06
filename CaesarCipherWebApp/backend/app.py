# backend/app.py

from flask import Flask, render_template, request, jsonify
from backend.caesar import caesar_cipher

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        message = data.get('message', '')
        shift_str = data.get('shift', '0')
        mode = data.get('mode', 'encrypt')

        try:
            shift = int(shift_str)
        except ValueError:
            return jsonify({'error': 'Shift value must be an integer.'}), 400

        if mode not in ['encrypt', 'decrypt']:
            return jsonify({'error': 'Invalid operation mode.'}), 400

        result_text = caesar_cipher(message, shift, mode)
        return jsonify({'result': result_text})

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
