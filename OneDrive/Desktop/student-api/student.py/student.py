from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    {"id": 1, "name": "Anja", "grade": 9},
    {"id": 2, "name": "Petar", "grade": 10}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    for s in students:
        if s['id'] == id:
            return jsonify(s)
    return jsonify({"error": "Student not found"}), 404

@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == '__main__':
    app.run(debug=True)
