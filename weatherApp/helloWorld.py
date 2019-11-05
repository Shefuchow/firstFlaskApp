# helloWorld.py
from flask import Flask           # import flask
helloWorld = Flask(__name__)      # create an app instance

@helloWorld.route("/")            # at the end point /
def hello():                      # call method hello
    return "Hello World! "        # which returns "hello world"


@helloWorld.route("/<name>")      # at the end point /<name>
def hello_name(name):             # call method hello_name
    return "Hello "+ name + "!"   # which returns "hello + name + !"


if __name__ == "__main__":        # on running python app.py
    helloWorld.run(debug=True)    # run the flask app
