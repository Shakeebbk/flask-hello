from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import requests
import json
import io
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret!"
bootstrap = Bootstrap(app)

params = {
            'format':'json',
            'api-key':'579b464db66ec23bdd000001cf238dae13894bfa7aca5db1bc9ea413',
         }
url = 'https://api.data.gov.in/resource/c500fb5d-4805-4d87-a806-4d99f761bb8d'

class LoginForm(Form):
    name = StringField("User", validators=[Required(),
                                           Length(1,16)])
    submit = SubmitField("Login")

@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()
    name = None
    if(form.validate_on_submit()):
        name = form.name.data
        form.name.data = ''
        return redirect('/report/'+name)
    return render_template('index.html', form=form)

@app.route("/report/<name>")
def report(name):
    data = requests.get(url=url, params=params)
    data = json.loads(data.text)
    resp = ''
    return render_template('report.html', items=data['records'], name=name)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
