from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests
import json
import io

app = Flask(__name__)
bootstrap = Bootstrap(app)

params = {
            'format':'json',
            'api-key':'579b464db66ec23bdd000001cf238dae13894bfa7aca5db1bc9ea413',
         }
url = 'https://api.data.gov.in/resource/c500fb5d-4805-4d87-a806-4d99f761bb8d'

@app.route("/")
def index():
    data = requests.get(url=url, params=params)
    data = json.loads(data.text)
    resp = ''
#    for items in data['records']:
#        resp += ("["+items['item']+"] ")+(items['percentage_growth_2001_02_to_2015_16_'])+"<br>"
    return render_template('index.html', items=data['records'])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
