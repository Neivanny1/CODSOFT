#!/usr/bin/python3
'''
Main app
'''
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from models import db, User, Task
from forms import LoginForm, RegisterForm, TaskForm
from auth import register_user, authenticate_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SECRET_KEY"] = "your-secret-key"
app.config["JWT_SECRET_KEY"] = "your-jwt-secret-key"
db.init_app(app)
jwt = JWTManager(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        register_user(form.username.data, form.password.data)
        flash("Account created successfully!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        token = authenticate_user(form.username.data, form.password.data)
        if token:
            flash("Login successful!", "success")
            return redirect(url_for("tasks"))
        else:
            flash("Invalid credentials.", "danger")
    return render_template("login.html", form=form)

@app.route('/tasks', methods=['GET', 'POST'])
@jwt_required()
def tasks():
    current_user = get_jwt_identity()
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            completed=form.completed.data,
            user_id=current_user
        )
        db.session.add(task)
        db.session.commit()
        flash("Task added!", "success")
        return redirect(url_for("tasks"))
    user_tasks = Task.query.filter_by(user_id=current_user).all()
    return render_template("tasks.html", form=form, tasks=user_tasks)

@app.route('/api/tasks', methods=['GET', 'POST'])
@jwt_required()
def api_tasks():
    current_user = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        task = Task(
            title=data['title'],
            description=data.get('description', ''),
            completed=data.get('completed', False),
            user_id=current_user
        )
        db.session.add(task)
        db.session.commit()
        return jsonify({"message": "Task created successfully"}), 201

    tasks = Task.query.filter_by(user_id=current_user).all()
    return jsonify([{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    } for task in tasks])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
