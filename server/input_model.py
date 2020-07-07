import io
import base64

from PIL import Image
from io import BytesIO


def convert_to_image(data: str):
    img_data = {"size": ""}
    image_data = base64.b64decode(data)
    img = Image.open(io.BytesIO(image_data))
    img_data["size"] = str(img.size)
    print("Original size: ", img.size)
    img = img.resize((128, 128))
    print("New size: ", img.size)
    img_data["msg"] = "Imagen recibida"
    img = img.convert("1")

    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_str = base64.b64encode(img_bytes.getvalue())
    img_data["data"] = img_str.decode('utf-8')
    img.close()
    img_bytes.close()

    return img_data
