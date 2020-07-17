from flask import Flask, request

from server.data import convert_to_image
from server.model import classify_image


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
            label = classify_image(img_data)
            img_data.close()
            resp["msg"] = label
            resp["size"] = img_data["size"]
            #resp["data"] = img_data["data"]

    return resp
