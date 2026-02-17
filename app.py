from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        flash("Form Submitted Successfully!")
        return render_template("contact.html")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
