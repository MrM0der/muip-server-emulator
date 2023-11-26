from flask import Flask, request
from anime_muip import AnimeMUIP
import json


accounts = {"MrModer": ["10.242.1.1", "10.242.11.11"]}


app = Flask(__name__)

client = AnimeMUIP(secret='', ip='10.242.1.1')


@app.route('/api', methods=['GET'])
def muip_server_emulator():
    client_ip = request.remote_addr  # Получение IP-адреса клиента
    uid = request.args.get('uid')
    msg = request.args.get('msg')
    print(f"IP-адрес клиента: {client_ip}")
    print(request)
    response = client.muip_client(uid, msg)
    response = json.loads(response)
    response["MuipServerEmulator"] = "Данный сервер был создан MrModer."
    response = json.dumps(response)
    print(response)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=21052)
