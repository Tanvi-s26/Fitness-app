from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        # We'll save to database on Day 3
        print(f"New user: {username}, {email}")
        return f"Welcome {username}! Database coming Day 3 😄"
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)