import flask
from flask import Flask, render_template


def score_server():
    app = Flask(__name__, template_folder='template')

    @app.route('/', methods=['GET', 'POST'])
    def hello_user():
        file = open("Scores.txt", 'r')
        word = file.readline()
        return flask.render_template('index.html', SCORE=word)

    app.run(host='127.0.0.1', debug=True, port=3000)




