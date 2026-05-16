from flask import Flask, render_template_string, request, redirect, url_for
import json
import os

app = Flask(__name__)

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# HTML template
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .task-form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        input[type="text"] {
            width: 70%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .task-list {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .task-item {
            padding: 10px;
            margin: 10px 0;
            background: #f9f9f9;
            border-left: 4px solid #4CAF50;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .delete-btn {
            background-color: #f44336;
            padding: 5px 10px;
            font-size: 12px;
        }
        .delete-btn:hover {
            background-color: #da190b;
        }
        .no-tasks {
            text-align: center;
            color: #999;
            padding: 20px;
        }
    </style>
</head>
<body>
    <h1>📝 Task Manager</h1>
    
    <div class="task-form">
        <form method="POST" action="/add">
            <input type="text" name="task" placeholder="Enter a new task..." required>
            <button type="submit">Add Task</button>
        </form>
    </div>
    
    <div class="task-list">
        <h2>Your Tasks</h2>
        {% if tasks %}
            {% for task in tasks %}
            <div class="task-item">
                <span>{{ task }}</span>
                <form method="POST" action="/delete/{{ loop.index0 }}" style="margin: 0;">
                    <button type="submit" class="delete-btn">Delete</button>
                </form>
            </div>
            {% endfor %}
        {% else %}
            <div class="no-tasks">No tasks yet. Add one above!</div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    """Display all tasks"""
    tasks = load_tasks()
    return render_template_string(HTML_TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    task = request.form.get('task')
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Run the app on all network interfaces and port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)