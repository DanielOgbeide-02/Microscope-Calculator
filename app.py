from flask import Flask, render_template, request, redirect, url_for
from database import init_db, save_measurement

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form["user"]
        mm   = float(request.form["mm"])
        mag  = float(request.form["mag"])
        act  = save_measurement(user, mm, mag)
        return render_template("index.html", result=act)
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
