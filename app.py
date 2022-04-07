from flask import Flask, render_template, request, flash
import bustimes

app = Flask(__name__)
app.secret_key = "not_very_secret"
@app.route("/bus-times")
def index():
    stops = bustimes.allCoachStnStops() if len(request.args) < 1 else stopsFromString(request.args.get("q"))
    buses = bustimes.getAllInfo(stops)
    
    for bus in buses:
        s = ""
        for attr in bus:
            s = s + "<td>" + attr + "</td>"
        flash(s)

    return render_template("index.html")


def stopsFromString(s):
    return [(stop.split(":")[0],stop.split(":")[1]) for stop in s.split(";")]

