from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
@app.route("/<name>")
def hello(name="Lechuan"):
    return f"Hello, {escape(name)}!"
