from flask import Flask, Response, request
import os
from urllib.parse import unquote

app = Flask(__name__)


# read the code...

@app.route("/", methods=["GET"])
def home(): return Response(open(__file__).read(), mimetype='text/plain')


@app.route("/read", methods=["GET"])
def get_file():
    return Response(open(unquote(request.args.get("file")).strip()).read(), mimetype='text/plain') if unquote(request.args.get("file")).strip() in [i.name for i in os.scandir()] and request.args.get("file") != "flag.txt" else "can't read this file..."

app.run(host="0.0.0.0" ,port=5001)
