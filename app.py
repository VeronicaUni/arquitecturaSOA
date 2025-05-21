from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://data-processor-v27b.onrender.com/api/data"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    data = request.get_json()
    print("Datos recibidos en Flask:", data)

    try:
        response = requests.post(API_URL, json=data)
        print("Respuesta de la API externa:")
        print("Status code:", response.status_code)
        print("Texto:", response.text)

        if response.status_code in [200, 201]:
            return jsonify({"mensaje": " Datos enviados correctamente"}), 200
        else:
            return jsonify({"mensaje": f"Error al enviar los datos. Código {response.status_code}"}), 500
    except Exception as e:
        return jsonify({"mensaje": f"Error de conexión: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
