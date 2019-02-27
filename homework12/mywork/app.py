from flask import Flask, render_template, request
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def form():
    return render_template('index.html')


@app.route("/result", methods=['POST'])
def result():
    from models import Inform
    zipCode = request.form['zipCode']

    key = 'AIzaSyCDKSQdglP_kfxPsZsDfqXxO0T193LJZfs'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyCDKSQdglP_kfxPsZsDfqXxO0T193LJZfs' % (
        zipCode)
    data = requests.get(url)
    print(data)

    if (data.status_code != 200):
        return 'Something wrong'
    else:
        lat = data.json()['results'][0]['geometry']['location']['lat']
        lng = data.json()['results'][0]['geometry']['location']['lng']
        address = data.json()['results'][0]['formatted_address']
        curr_inform = Inform(zipCode=zipCode, lat=lat, lng=lng, address=address)

        db.session.add(curr_inform)
        db.session.commit()
        return render_template('result.html', curr_inform=curr_inform)



if __name__ == "__main__":
    app.run(debug=True)
