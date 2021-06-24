from flask import Flask, jsonify, abort, make_response, Response, request
import requests
import os

app = Flask(__name__)

data = [{
    'id':1,
    'name':'ata'
    }, {
    'id':2,
    'name':'tolga'
    }
]

@app.route("/")
def index():
    return jsonify({'yarin pompa mi var':'evet'})

@app.route('/<int:userid>', methods=['GET'])
def getUser(userid):    
    for item in data:
        if item['id'] == userid:
            return jsonify(item)
    abort(404, 'User not found')

@app.route('/add', methods=['POST'])
def addUser():
    name = request.form['name']
    curid = data[-1]['id'] + 1
    item = {'id':curid, 'name':name}
    data.append(item)
    return jsonify(item), 201

@app.errorhandler(404)
def not_found(error):
    return make_response({'error': error.description}, 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
