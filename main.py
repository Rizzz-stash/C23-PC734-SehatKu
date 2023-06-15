import csv
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask import Flask, request, jsonify
from './Notebooks' import predict, predict_ocr


NUM_WORDS = 30000
EMBEDDING_DIM = 100
MAXLEN = 100
PADDING = 'post'
OOV_TOKEN = "<OOV>"
TRAIN_FILE = "./dataset/processed_train.csv"  # cloud storage url
STOPWORDS_FILE = "./dataset/stopwordbahasa.csv"  # cloud storage url
STOPWORDS = []

app = Flask(__name__)


@app.route("/predict", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ubah data ke image
        image = request.files['image']
        if image is None:
            return jsonify({"error": "No image"})

        try:
            # Train image data menggunakan fungsi
            hasil = predict(image)

            data = {"prediction": hasil}

            return jsonify(data)

        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"


@app.route("/predict-ocr", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Ubah data ke image
        image = request.files['image']
        if image is None:
            return jsonify({"error": "No image"})

        try:
            # Train image data menggunakan fungsi
            hasil = predict_ocr(image)

            data = {"prediction": hasil}

            return jsonify(data)

        except Exception as e:
            return jsonify({"error": str(e)})

    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
