# GPT-3 Generation of Code

Write a Python script that reads a CSV file from the filesystem and exposes an API on it with GET, POST, and LIST methods. Changes made through the API should be reflected in the CSV file.

The CSV file students.csv contains only three columns: id,name,email

a sample CSV file with 10 entries looks like this:

-- AI GENERATED TEXT START --
```
id,name,email
1,John Doe,john@example.com
2,Jane Doe,jane@example.com
3,Bob Smith,bob@example.com
4,Alice Smith,alice@example.com
5,Mike Jones,mike@example.com
6,Sally Jones,sally@example.com
7,Joe Brown,joe@example.com
8,Sue Brown,sue@example.com
9,Bill Black,bill@example.com
10,Sue Black,sue@example.com

```
the API should support the following methods:

GET /student/<id>
returns a JSON object with the student's information

POST /student
creates a new student with the information provided in the request body

GET /students
returns a JSON array with all students

-- AI GENERATED TEXT END --



from flask import request, jsonify, abort, Flask, make_response
import csv, os

-- AI GENERATED TEXT START --


```
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
    app.run(p)

```
-- AI GENERATED TEXT END --


write a sample curl request that creates a new student

-- AI GENERATED TEXT START --


curl -X POST -H "Content-Type: application/json" -d '{"id": "11", "name": "John Doe", "email": "john@example.com"}' http://localhost:5000/student

write a sample curl request that lists all students

curl -X GET http://localhost:8080/students

write a sample curl request that gets a student by id

curl -X GET http://localhost:5000/student/1

-- AI GENERATED TEXT END --
