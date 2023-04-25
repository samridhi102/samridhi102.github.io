import pickle
import cv2
import flask
import numpy as np
import werkzeug
from flask import send_from_directory, request, render_template, jsonify
import os
app = flask.Flask(__name__)

model = pickle.load(open('svm_model.pkl', 'rb'))

dic = ['Oral Cancer Not Detected', 'Oral Cancer Detected']


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Welcome"


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/predict/', methods=['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image0']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    img = cv2.imread(filename)
    img = cv2.resize(img, (128, 128))
    flattened = img.flatten()
    img = np.array(flattened)
    img = img.reshape(1, -1)
    print("Later: ", img.shape)
    predicted_label = model.predict(img)
    # predicted_label = np.argmax(model.predict(np.array([img]))[0], axis=1)
    print(predicted_label)
    return dic[predicted_label[0]]


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=os.environ.get('PORT', 5000), debug=True)
    app.run(host="0.0.0.0", port=os.environ.get('PORT', 5000), debug=True)

