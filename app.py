import json
import pickle

from flask import Flask, Response, render_template, request, url_for
from PIL import Image
from models.model1 import model1_predictor
from models.model2 import model2_predictor
from models.model3 import model3_predictor

app = Flask(__name__)

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

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
            del fname
            return resp
        except Exception as e:
            data = {
                'error_message': "some error occured, ensure your image is small and jpg"
            }
            js = json.dumps(data)
            resp = Response(js, status=400, mimetype='application/json')
            del fname
            return resp
    elif request.method == 'GET':
        return render_template('cat.html')

@app.route('/handdigit', methods=['GET', 'POST'])
def api2():
    if request.method == 'POST':
        email = request.form.get('email','')
        fname = request.files['image']
        res = Response()
        try:
            p = model2_predictor(fname)
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
    elif request.method == 'GET':
        return render_template('hand.html')

@app.route('/smilenotsmile', methods=['GET', 'POST'])
def api3():
    if request.method == 'POST':
        email = request.form.get('email','')
        fname = request.files['image']
        print(type(fname))
        res = Response()
        try:
            p = model3_predictor(fname)
            a = int(p[0])
            data = {
                'prediction': a
            }
            js = json.dumps(data)
            resp = Response(js, status=200, mimetype='application/json')
        except Exception as e:
            data = {
                'error_message': "some error occured, ensure your image is small and jpg"
            }
            js = json.dumps(data)
            resp = Response(js, status=400, mimetype='application/json')
        
        return resp
    elif request.method == 'GET':
        return render_template('smilenotsmile.html')

# with app.test_request_context():
#     print(url_for('hello_world'))
#     print(url_for('api1'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
