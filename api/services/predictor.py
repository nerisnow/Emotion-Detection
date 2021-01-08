import flask
from flask import request, render_template
from emotiondetection.main import test_pipeline
from api.config import config

from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request


def home():
    return render_template("index.html")


def sentence_prediction(sentence):
    output = test_pipeline(config.MODEL[1], input_text=sentence)
    return output


def predict():
    payload = request.form["review"]
    print("[INFO: (api/service/predictor)]: User feedback received")
    prediction = sentence_prediction(payload)
    return render_template("predict.html", input_text=payload, output=prediction)


def data():

    # POST a data to database
    if request.method == "POST":
        body = request.json
        name = body["name"]
        age = body["age"]

        # db.users.insert_one({
        db["users"].insert_one({"name": name, "age": age})
        return jsonify(
            {"status": "Data is posted to MongoDB!", "name": name, "age": age}
        )

    # GET all data from database
    if request.method == "GET":
        allData = db["users"].find()
        dataJson = []
        for data in allData:
            id = data["_id"]
            name = data["name"]
            age = data["age"]
            dataDict = {"id": str(id), "name": name, "age": age}
            dataJson.append(dataDict)
        print(dataJson)
        return jsonify(dataJson)
