from flask import Flask, Response, render_template_string, request

app = Flask(__name__)

@app.route("/")
def home():
    return Response(open(__file__).read(), mimetype='text/plain')


@app.route("/name", methods=["GET"])
def name():
    name = request.args.get("name")
    return render_template_string(f"Hello! {name}.")


app.run()
