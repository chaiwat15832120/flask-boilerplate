from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "sam sam sam sam sam"

@app.route('/new_one')
def new_one_function():
    username = request.args.get('name')
    print(username)
    return 'Hi '+username
    #new_one?name=chaiwat

@app.route('/sum')
def my_sum():
    a = request.args.get('a')
    a=int(a)
    b = request.args.get('b')    
    b=int(b)
    return str (a+b)
    #sum?a=1&b=2

@app.route('/mypage')
def mypage():
    username = request.args.get('name')
    return render_template('home.html', name=username)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)