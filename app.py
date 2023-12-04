from flask import Flask, jsonify, request, json
import random, base64

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_home_handler():
    return jsonify({"success": True, "msg": "ML Rest API"}), 200

@app.route("/predict", methods=["POST"])
def preidct_handler():
    req = json.loads(request.data)
    data = req["data"]
    b64_img_data = data["b64_img_data"]
    decoded_data = base64.b64decode(b64_img_data)
    filename = data["filename"]

    # for debugging, uncomment to save the file from decoded b64
    # with open(filename, "wb") as f:
    #     f.write(decoded_data)

    # TODO: Image processing here
    
    return jsonify({"success": True, "msg": f"prediction is {random.randint(1,100)}"}), 200

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)