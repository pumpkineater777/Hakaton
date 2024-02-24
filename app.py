#!flask/bin/python
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

cur_id = 0
data = []


def stop_it(id):
    pass

@app.route("/temp", methods=['GET'])
def temp():
    return jsonify(data), 201

@app.route('/api/partners', methods=['POST'])
def create_partner():
    global cur_id
    data.append({
        'id': cur_id,
        'name': request.json["name"],
        'budget': request.json["budget"],
        'spent_budget': 0,
        'is_stopped': False,
        'dates': []
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
    temp['id'] = data[id]['id']
    temp['name'] = data[id]['name']
    temp['budget'] = data[id]['budget']
    temp['spent_budget'] = data[id]['spent_budget']
    temp['is_stopped'] = data[id]['is_stopped']
    return jsonify(temp), 201


@app.route('/api/partners/<int:id>/cashback', methods=['PUT'])
def update_info(id):
    data[id]['spent_budget'] += request.json["cashback"]
    data[id]['dates'].append([request.json["date"].split()[0], request.json["cashback"]])
    stop_it(id)
    return jsonify({"ok": "ok"}), 201

@app.route('/home')
def home():
    return render_template('Main.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
# curl -i -H "Content-Type: application/json" -X POST --data "{"""name""":"""VTB""","""budget""":10002}" http://localhost:8080/api/partners
# curl -i http://localhost:8080/api/partners/0
# curl -i -H "Content-Type: application/json" -X PUT --data "{"""date""":"""2023-02-0200:00:00""","""name""":"""VTB""","""cashback""":23232.34}" http://localhost:8080/api/partners/0/cashback
