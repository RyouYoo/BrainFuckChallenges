from flask import Flask, request, make_response, jsonify, render_template, Response
import random
import base64
import json

# don't fall into the rabbit hole

with open("./config.json", "r") as config:
    FLAG = json.load(config)["FLAG"]

def set_keys():
    with open("./rockyou.txt", "r") as rockyou: k = [rockyou.readline(i).strip("\n") for i in range(1,101)]
    return dict(zip(random.sample(k, len(FLAG)), FLAG))


data = set_keys()

app = Flask(__name__)

@app.route("/")
def home():
    return Response(open(__file__).read(), mimetype='text/plain')

@app.route("/check", methods=["POST"])
def code_str():
    l = base64.b64decode(request.form["key"].encode('ascii')).decode('utf-8')
    return make_response(jsonify({"message": data[l]}), 200) if l in list(data.keys()) else make_response(jsonify({"message": "0"}), 404)

@app.route("/check_flag", methods=["POST"])
def check_flag():
    return FLAG if sorted(list(request.form["chars"])) == sorted(list(data.values())) else "0"


app.run(host="0.0.0.0", port=5000)
