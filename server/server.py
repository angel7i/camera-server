from flask import Flask, request

from server.input_model import convert_to_image


app = Flask(__name__)

app.config.update(
    ENV='development ')


@app.route('/', methods=['GET'])
def about():
    return "Welcome to camera-server!"


@app.route('/image', methods=['POST'])
def process_image():
    resp = {"msg": "No se adjunto imagen"}
    req_data = request.get_json()

    if req_data:
        if 'data' in req_data:
            img_data = convert_to_image(req_data['data'])
            resp["size"] = img_data["size"]
            resp["msg"] = img_data["msg"]
            resp["data"] = img_data["data"]

    return resp
