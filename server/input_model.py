import io
import base64

from PIL import Image

def convert_to_image(data: str):
    image_data = base64.b64decode(data)
    img = Image.open(io.BytesIO(image_data))
    print("Original size: ", img.size)
    img = img.resize((128, 128))
    #img.save('temp.png', 'png')

    return img