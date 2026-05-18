from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import db, User
from models.workout import Workout, Follow
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template("register.html", error="Email already registered!")
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            return render_template("login.html", error="Invalid email or password!")
        login_user(user)
        return redirect(url_for("dashboard"))
    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    workouts = Workout.query.filter_by(user_id=current_user.id)\
               .order_by(Workout.created_at.desc()).limit(5).all()

    total_workouts = Workout.query.filter_by(user_id=current_user.id).count()
    total_calories = db.session.query(db.func.sum(Workout.calories))\
                    .filter_by(user_id=current_user.id).scalar() or 0
    total_minutes = db.session.query(db.func.sum(Workout.duration))\
                   .filter_by(user_id=current_user.id).scalar() or 0

    following = Follow.query.filter_by(follower_id=current_user.id).all()
    following_ids = [f.following_id for f in following]
    feed = Workout.query.filter(Workout.user_id.in_(following_ids))\
           .order_by(Workout.created_at.desc()).limit(10).all()

    return render_template("dashboard.html",
        workouts=workouts,
        feed=feed,
        total_workouts=total_workouts,
        total_calories=total_calories,
        total_minutes=total_minutes
    )

@app.route("/log-workout", methods=["GET", "POST"])
@login_required
def log_workout():
    if request.method == "POST":
        workout = Workout(
            user_id=current_user.id,
            workout_type=request.form["workout_type"],
            duration=int(request.form["duration"]),
            calories=int(request.form["calories"]),
            notes=request.form.get("notes", "")
        )
        db.session.add(workout)
        db.session.commit()
        return render_template("log_workout.html", success="Workout logged successfully! 💪")
    return render_template("log_workout.html")

@app.route("/users")
@login_required
def users():
    all_users = User.query.filter(User.id != current_user.id).all()
    return render_template("users.html", users=all_users)

@app.route("/follow/<int:user_id>")
@login_required
def follow(user_id):
    existing = Follow.query.filter_by(
        follower_id=current_user.id,
        following_id=user_id
    ).first()
    if not existing:
        follow = Follow(follower_id=current_user.id, following_id=user_id)
        db.session.add(follow)
        db.session.commit()
    return redirect(url_for("users"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)