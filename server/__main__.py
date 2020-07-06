from flask import Flask, request

from input_model import convert_to_image


app = Flask(__name__)

app.config.update(
    ENV='development ')

@app.route('/', methods=['GET'])
def about():
    return "OK!"

@app.route('/image', methods=['POST'])
def get_image():
    req_data = request.get_json()

    if  'data' in req_data:
        img = convert_to_image(req_data['data'])
        print("New size: ", img.size)
        img.close()
        
    return {"msg": "OK!"}


if __name__ == "__main__":
    app.run(host= '0.0.0.0')
    print("Starting server")