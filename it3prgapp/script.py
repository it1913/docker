from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def ahoj():
    return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    pole=["jedna","dvě","tři"]
    return render_template('script.html', pole=pole, name=name)