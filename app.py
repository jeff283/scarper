from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests


from flask import Flask,  render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download')
def download():


    url = "https://fmmods.com/fouad-whatsapp/"
    site = requests.get(url).text

    soup = BeautifulSoup(site, features="lxml")

    data = soup.select("div>a[onclick^='downloadpage']")

    data = data[0]["onclick"]
    data = data.split('\n')[1].strip().rstrip("',").lstrip("'")

    return redirect(data)
       
if __name__ == '__main__':
    app.run(debug=False)
    