from flask import Flask

app = Flask(__name__) 

@app.route('/') # www.domain.com
def index():
    return "<h1>Todo index page</h1>"

@app.route('/tasks')
def all_tasks():
    return "<h1>List of all tasks</h1>"
    
@app.route('/task/<taskid>') #www.domain.com/taslk/1 - enforce an integer with: <int:task_id>
def task(task_id):
    return "<h1>Task detail page for task {task_id}<h1>"

@app.route('/new-task')
def new_task():
    return "<h1>This is a new task</h1>"

