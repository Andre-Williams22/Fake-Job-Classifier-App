from flask import Flask

app = Flas(__name__)


@app.route('/')
def index():
    return '<h1> Andre this is deployed!!! </h1>'