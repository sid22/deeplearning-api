import json
import pickle

from flask import Flask, Response, render_template, request, url_for

from models.model1 import model1_predictor

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
    elif request.method == 'GET':
        return render_template('cat.html')

# with app.test_request_context():
#     print(url_for('hello_world'))
#     print(url_for('api1'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
