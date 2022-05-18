import csv, os
from waitress import serve
from flask import request, jsonify, abort, Flask, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/student/<id>', methods=['GET'])
def get_student(id):
    with open('students.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] == id:
                return jsonify(row)
        abort(404)

@app.route('/student', methods=['POST'])
def create_student():
    if not request.json or not 'name' in request.json:
        abort(400)
    with open('students.csv', 'a') as csvfile:
        fieldnames = ['id', 'name', 'email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': request.json['id'], 'name': request.json['name'], 'email': request.json['email']})
    return jsonify({'result': True}), 201

@app.route('/students', methods=['GET'])
def get_students():
    with open('students.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        students = []
        for row in reader:
            students.append(row)
        return jsonify(students)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
	# Dev
	# app.run(port=8080)

	serve(app, host="0.0.0.0", port=8080)
