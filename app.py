#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)

cur_id = 0
data = []


# hostname = cashback

def stop_it(id):
    pass

@app.route('/api/partners', methods=['POST'])
def create_partner():
    global cur_id
    data.append({
        'id': cur_id,
        'name': request.json['name'],
        'budget': request.json['budget'],
        'spent_budget': 0,
        'is_stopped': False,
        'data': []
    })
    cur_id += 1
    temp = dict()
    temp['id'] = data[-1]['id']
    temp['name'] = data[-1]['name']
    temp['budget'] = data[-1]['budget']
    temp['spent_budget'] = data[-1]['spent_budget']
    return jsonify(temp), 201


@app.route('/api/partners/<int:id>', methods=['GET'])
def get_info(id):
    temp = dict()
    temp['id'] = data[-1]['id']
    temp['name'] = data[-1]['name']
    temp['budget'] = data[-1]['budget']
    temp['spent_budget'] = data[-1]['spent_budget']
    temp['is_stopped'] = data[-1]['is_stopped']
    return jsonify(temp), 201


@app.route('/api/partners/<int:id>/cashback', methods=['PUT'])
def update_info(id):
    data[id]['spent_budget'] += request.json["cashback"]
    data[id]['data'].append([request.json["data"].split()[0], request.json["cashback"]])
    stop_it(id)

if __name__ == '__main__':
    app.run(debug=True)
