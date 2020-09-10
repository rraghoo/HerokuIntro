from flask import Flask, render_template
#import datetime


app = Flask(__name__)

@app.route("/")
def index():
 #   some_text = "Message from the handler"
    return render_template("index.html")

@app.route("/about-me")
def about_me():
    return render_template("about.html")

if __name__ == '__main__':
    app.run()