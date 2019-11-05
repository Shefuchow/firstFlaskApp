# helloWorld.py
from flask import Flask           # import flask
helloWorld = Flask(__name__)      # create an app instance

@helloWorld.route("/")            # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    helloWorld.run()              # run the flask app