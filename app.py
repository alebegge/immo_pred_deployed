import json
from datetime import datetime
from flask import Flask, request, jsonify, abort
from predict.prediction import predict
from preprocessing.cleaning_data import preprocess

app = Flask(__name__)

@app.route('/', methods=["GET"])
def alive():
    return f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - This server is alive."

@app.route('/predict', methods=["GET", "POST"])
def predicted():
    error = None
    input_json = request.get_json(force=True)
    if request.method == 'POST':
        data_prep = preprocess(input_json["data"])
        if data_prep:
            return str(predict(data_prep))
        else:
            error = 'Invalid data, please refer to the documentation.'
            return error
    if request.method == 'GET':
        return doc
    else:
        error = 'This route only takes POST as method for now.'
        return error


doc ="""
{
  "data": 
  {
    "area": int,
    "property-type": "APARTMENT" | "HOUSE" | "OTHERS",
    "rooms-number": int,
    "zip-code": int,
    "land-area": Optional[int],
    "garden": Optional[bool],
    "garden-area": Optional[int],
    "equipped-kitchen": Optional[bool],
    "full-address": Optional[str],
    "swimming-pool": Optional[bool],
    "furnished": Optional[bool],
    "open-fire": Optional[bool],
    "terrace": Optional[bool],
    "terrace-area": Optional[int],
    "facades-number": Optional[int],
    "building-state": Optional[
      "NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"
    ]
  }
} """

if __name__ == '__main__':
    app.run(port=5000, debug=True)