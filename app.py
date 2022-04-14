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

    try:
        url = "https://fmmods.com/fouad-whatsapp/"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
        site = requests.get(url, headers=headers).text

        soup = BeautifulSoup(site, features="lxml")

        data = soup.select("div>a[onclick^='downloadpage']")

        data = data[0]["onclick"]
        data = data.split('\n')[1].strip().rstrip("',").lstrip("'")

        return redirect(data)
    except Exception as e:
        print(e)
        return render_template('error.html'), 500

       
if __name__ == '__main__':
    app.run(debug=True)
    