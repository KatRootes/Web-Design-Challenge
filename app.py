import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data")
def data():
    path = "Resources/cities.csv"
    df = pd.read_csv(path)
    html = df.to_html().replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    f = open('Resources/cities.html','w')
    f.write(html)
    f.close()
    return html