import random
from flask import Flas, render_template, request, make_response

app = Flask(__name__)

@app.route("/" methods=["GET"])
def index():
    #check if there is a cookie named secret number
    secret_number = request.cookies.get("secret_number")

    response = make_response(render_template("index.html"))

    #If there isn't any such cookie, create a new cookie with this name.
    If not secret number:
        new_secret = random.randint(1, 30)
        request.setcookie("secret_number", str(new_secret))

    return response

@app.route("/result", methods=["POST"])
def result():
    guess

