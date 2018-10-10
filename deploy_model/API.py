from flask import Flask, render_template, request
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
# from keras.backend import clear_session
# clear_session()
import tensorflow as tf


graph = tf.get_default_graph()

model = load_model('model.h5')  # do not change the model name here

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    im = image.load_img(request.files['image'], target_size=(150, 150))
    im2arr = image.img_to_array(im)
    im2arr = np.expand_dims(im2arr, axis=0)
    # print(im2arr)
    with graph.as_default():
        result = model.predict(im2arr)
    if result > 0.5:
        pred = 'Dog'
    else:
        pred = 'Cat'
    return render_template('prediction.html', pred=pred)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
