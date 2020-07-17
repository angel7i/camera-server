import tensorflow as tf
import numpy as np

from tensorflow import keras
from keras.preprocessing.image import img_to_array


model = keras.models.load_model('model.h5')

classes = ["Circulo", "Cuadrado", "Triangulo"]

def classify_image(img):
    x = img_to_array(img) / 255
    #x = x.reshape((1, 150, 150, 1))
    print("Array:", x.shape)

    try:
        prediction = model.predict(np.array([x]))
        print(prediction)
        index = np.argmax(prediction)
        print(index)
    except ValueError as e:
        print(e)
        return "La imagen no es reconocida"   

    return classes[index]