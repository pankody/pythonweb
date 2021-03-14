from flask import Flask

app = Flask(__name__)


# @app.route("/")
# def HelloWorld():
#     a = 1
#     b = 1
#     c = a / b  
#     return "HelloWorld!"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9090, debug=True)
