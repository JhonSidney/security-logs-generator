import random
from flask import Flask, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/computers', methods=['GET'])
def obter_informacoes_deepsecurity():
    pass

if __name__ == '__main__':
    app.run(debug=True)