from flask import Flask, request, jsonify
from database import save_message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        
        if not all([name, email, message]):
            return jsonify({'error': 'Tous les champs sont requis'}), 400
        
        save_message(name, email, message)
        return jsonify({'message': 'Message envoyé avec succès'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000) 