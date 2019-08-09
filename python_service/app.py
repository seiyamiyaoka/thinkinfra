from flask import Flask

app = Flask(__name__)
# env FLASK_APP=app.py flask run http://127.0.0.1:5000
@app.route("/")
def hello():
    return "python yade"