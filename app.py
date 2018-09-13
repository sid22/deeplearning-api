from flask import Flask
from flask import Response
from flask import request
from flask import render_template

from models.model1 import model1_predictor
import json
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')    
    # return 'Hello, World!'

@app.route('/catnoncat', methods=['GET', 'POST'])
def api1():
    if request.method == 'POST':
        email = request.form.get('email','')
        fname = request.files['image']
        res = Response()
        def_label = 0
        try:
            p = model1_predictor(fname, def_label)
            data = {
                'prediction': p
            }
            js = json.dumps(data)
            resp = Response(js, status=200, mimetype='application/json')
            return resp
        except Exception as e:
            data = {
                'error_message': "some error occured, ensure your image is small and jpg"
            }
            js = json.dumps(data)
            resp = Response(js, status=400, mimetype='application/json')
            return resp

if __name__ == "__main__":
    app.run(debug=True, port=5000)