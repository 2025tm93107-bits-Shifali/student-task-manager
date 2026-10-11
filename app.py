from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Jenkins", "completed": False},
    {"id": 2, "title": "Run SonarQube", "completed": True}
]

@app.route("/")
def home():
    completed = sum(task["completed"] for task in tasks)
    return render_template("index.html", tasks=tasks, completed=completed)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title")
    if title:
        tasks.append({"id": len(tasks) + 1, "title": title, "completed": False})
    return redirect("/")

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
    return redirect("/")

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)