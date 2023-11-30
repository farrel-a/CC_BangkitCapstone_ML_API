from flask import Flask, jsonify, request, json
import random

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_home_handler():
    return jsonify({"success": True, "msg": "ML Rest API"}), 200

@app.route("/predict", methods=["POST"])
def preidct_handler():
    req = json.loads(request.data)
    return jsonify({"success": True, "msg": f"prediction is {random.randint(1,100)}", "data" : req["data"]}), 200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)