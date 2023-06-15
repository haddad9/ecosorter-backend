import os
import json
# Flask
from flask import Flask,request, render_template, jsonify
from gevent.pywsgi import WSGIServer
from flask_cors import CORS


# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from util import base64_to_pil


app = Flask(__name__)
CORS(app)
MODEL_PATH = 'models/model.h5'

# Load your own trained model
model = load_model(MODEL_PATH)
model.make_predict_function()          # Necessary
print('Model loaded. Start serving...')


def model_predict(img, mdl):
    img = img.resize((192, 192))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = img_array.astype('uint8')  # Convert to unsigned integer type
    predictions = mdl.predict(tf.expand_dims(img_array, 0))
    score = tf.nn.sigmoid(predictions[0])   # Apply a sigmoid since our model returns logits
    score = tf.where(score < 0.5, 0, 1)
    score = score.numpy()
    class_result = "B" if score == 0 else "N"
    return class_result


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        json_img = json.loads(json.dumps(request.json))
        print(json_img)
        f = open("tes.txt", "a")
        f.write(str(json_img))
        f.close()

        img = base64_to_pil(json_img["image"])
        print('Model loaded. Check {}:8080/', request.host_url)
        print(type(img))
        # Save the image to ./uploads
        # img.save("./uploads/image.png")
        
        # Make prediction
        preds = model_predict(img, model)
        return jsonify(result=preds)


    return None


@app.route('/predict-img', methods=['GET', 'POST'])
def predict_web():
    if request.method == 'POST':
        img = base64_to_pil(request.json)
        print('Model loaded. Check {}:8080/', request.host_url)
        print(type(img))
        # Save the image to ./uploads
        # img.save("./uploads/image.png")
        
        # Make prediction
        preds = model_predict(img, model)
        return jsonify(result=preds)


    return None

if __name__ == '__main__':
    http_server = WSGIServer(('', int(os.environ.get('PORT', 8080))), app)
    http_server.serve_forever()
