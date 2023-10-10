from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from pre_process import pre_process
from load_data import load_image
import os

app = Flask(__name__)

model = load_model("modele_de_reseau.h5")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        file = request.files['file']
        print("file : ", file)
        file_path = "temp_image.jpg"
        file.save(file_path)

        img = load_image(file_path)
        print("img : ", img)

        processed_image = pre_process(img)

        print("processed image : ", processed_image)
        prediction = model.predict(processed_image)

        if prediction > 0.5:
            result = "Pneumonia"
        else:
            result = "Normal"

        os.remove(file_path)

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)