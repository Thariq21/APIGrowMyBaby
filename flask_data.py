from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

# Array untuk menyimpan data
data_store = []

@app.route('/data', methods=['POST'])
def save_data():
    # Mendapatkan data dari request
    data = request.get_json()

    # Menyimpan data di array
    if len(data_store) == 0:
        data_store.append(data)
    else:
        data_store[0] = data
    
    return jsonify({"message": "Data berhasil disimpan", "data": data}), 201

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store), 200

if __name__ == '__main__':
    # Mendapatkan hostname perangkat
    hostname = socket.gethostname()
    # Mendapatkan IP lokal perangkat
    local_ip = socket.gethostbyname(hostname)
    
    # Menjalankan server pada semua antarmuka jaringan
    app.run(host='0.0.0.0', port=5000, debug=True)
