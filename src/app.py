from flask import Flask, render_template, request, flash
import bustimes

app = Flask(__name__)
app.secret_key = "not_very_secret"
@app.route("/bus-times")
def index():
    buses = bustimes.getAllInfo(bustimes.allCoachStnStops())

    for bus in buses:
        s = ""
        for attr in bus:
            s = s + "<td>" + attr + "</td>"
        flash(s)

    return render_template("index.html")


