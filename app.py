from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/data')
def data():
    with open('data.json') as f:
        data = json.load(f)
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
