from flask import Flask, render_template, redirect, request, flash, url_for

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/")
def ahoj():
    return "Hello World!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    pole=["jedna","dvě","tři"]
    return render_template('script.html', pole=pole, name=name)

from wtforms import Form, BooleanField, StringField, PasswordField, validators, FloatField


class RegistrationForm(Form):
    a = FloatField('Value a', [validators.number_range(0,10)])
    b = FloatField('Value b', [validators.number_range(0,10)])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
        return str(int(form.a.data) + int(form.b.data))
    return render_template('register.html', form=form)
