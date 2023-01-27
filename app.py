from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def get_data():
    return "Hello World!555"

@app.route('/data')
def hello():
    return [{"name":"maya"},{"name":"vick"},{"name":"ido"}]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
