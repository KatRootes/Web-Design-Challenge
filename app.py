import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("data")
def data():
    path = "/Resources/cities.csv"
    df = pd.read_csv(path)
    html = pd.DataFrame.to_html(df)
    return html