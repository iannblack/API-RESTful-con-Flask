from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.get_json()
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if task_id >= len(tasks):
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(tasks[task_id]), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id >= len(tasks):
        return jsonify({"error": "Tarea no encontrada"}), 404
    tasks[task_id] = request.get_json()
    return jsonify(tasks[task_id]), 200

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id >= len(tasks):
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(tasks.pop(task_id)), 200

if __name__ == '__main__':
    app.run(debug=True)
