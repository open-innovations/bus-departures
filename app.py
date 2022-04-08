from flask import Flask, render_template, request, flash
import bustimes

app = Flask(__name__)
app.secret_key = "not_very_secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bus-times")
def busTimes():
    stops = bustimes.allCoachStnStops() if len(request.args) < 1 else stopsFromString(request.args.get("q"))
    return renderPageFromStops(stops,"Custom")

@app.route("/leeds-city-bus-station")
def showPage1():
    prefix = "Stand "
    stops = stopsFromString("""1:45030220;2:45030221;3:45030222;4:45030223;5:45030224;6:45030225;7:45030226;
    8:45030227;9:45030228;10:45030229;11:45030230;12:45030231;13:45030232;14:45030233;15:45030234;
    16:45030235;17:45030236;18:45030237;19:45030238;20:45030239;21:45030240;22:45030241""",prefix)

    return renderPageFromStops(stops,"Leeds City Bus Station")


@app.route("/leeds-corn-exchange-bus-point")
def showPage2():
    prefix = "Stand "
    stops = stopsFromString("""A:45010684;B:45010683;C:45012980;D:45010684;E:45012982;
    F:45012984;G:45014779;H:45032247;I:45012652""",prefix)

    return renderPageFromStops(stops,"Leeds Corn Exchange Bus Point")


@app.route("/leeds-bradford-airport-bus-point")
def showPage4():
    prefix = "Stand "
    stops = stopsFromString("""1:45025387;2:45025386;3:45028272""",prefix)

    return renderPageFromStops(stops,"Leeds Bradford Airport Bus Point")  

@app.route("/leeds-station-interchange")
def showPage5():
    prefix = "Stand "
    stops = stopsFromString("""A:45025479;B:45025478;C:45025477;D:45011026""",prefix)

    return renderPageFromStops(stops,"Leeds Station Interchange")  

@app.route("/leeds-infirmary-street-bus-point")
def showPage6():
    prefix = "Stand "
    stops = stopsFromString("""A:45025317;B:45025318;C:45032241;D:45032242;E:45032243""",prefix)

    return renderPageFromStops(stops,"Leeds Infirmary Street Bus Point")

@app.route("/white-rose-centre-bus-point")
def showPage12():
    prefix = "Stand "
    stops = stopsFromString("""A:45025310;B:45025311;C:45025312;D:45025313;E:45025314;F:45025315;G:45025316;H:45025352""",prefix)

    return renderPageFromStops(stops,"White Rose Centre Bus Point")      

@app.route("/bramley-centre-bus-station")
def showPage3():
    prefix = "Stand "
    stops = stopsFromString("""A:45012790;B:45012791;C:45012792;D:45012793;E:45012795""",prefix)

    return renderPageFromStops(stops,"Bramley Centre Bus Station")    

@app.route("/morley-town-hall-hub")
def showPage7():
    prefix = "Stand "
    stops = stopsFromString("""A:45010338;B:45010339;C:45010340;D:45010341;E:45010342""",prefix)

    return renderPageFromStops(stops,"Morley Town Hall Hub")  

@app.route("/otley-bus-station")
def showPage8():
    prefix = "Stand "
    stops = stopsFromString("""1:45025305;2:45025306;3:45025305;4:45025308;5:45010478""",prefix)

    return renderPageFromStops(stops,"Otley Bus Station")  

@app.route("/pudsey-bus-station")
def showPage9():
    prefix = "Stand "
    stops = stopsFromString("""A:45026239;B:45026240;C:45026241;D:45026242;E:45026243;F:45026244""",prefix)

    return renderPageFromStops(stops,"Pudsey Bus Station")  

@app.route("/seacroft-bus-station")
def showPage10():
    prefix = "Stand "
    stops = stopsFromString("""A1:45028111;B:45025301;C:45025302;D:45025303;E:45025304""",prefix)

    return renderPageFromStops(stops,"Seacroft Bus Station")  

@app.route("/wetherby-bus-station")
def showPage11():
    prefix = "Stand "
    stops = stopsFromString("""A:45025353;B:45014895""",prefix)

    return renderPageFromStops(stops,"Wetherby Bus Station") 

@app.route("/halifax-bus-station")
def showPage13():
    prefix = "Stand "
    stops = stopsFromString("""A:45032309;B:45032310;C:45032311;D:45032312;E:45032313;F:45032314""",prefix)

    return renderPageFromStops(stops,"Halifax Bus Station")

@app.route("/brighouse-bus-station")
def showPage14():
    prefix = "Stand "
    stops = stopsFromString("""A:45030120;B:45030330;C:45030329;D:45030328;E:45030121;F:45030119""",prefix)

    return renderPageFromStops(stops,"Brighouse Bus Station")

@app.route("/todmorden-bus-station")
def showPage15():
    prefix = "Stand "
    stops = stopsFromString("""A:45023172;B:45023173;C:45023174;D:45023175;E:45023176""",prefix)

    return renderPageFromStops(stops,"Todmorden Bus Station")


def renderPageFromStops(stops,stationName):
    buses = bustimes.getAllInfo(stops)
    
    for bus in buses:
        s = ""
        for attr in bus:
            s = s + "<td>" + attr + "</td>"
        flash(s)

    return render_template("bus-times.html",station=stationName)


def stopsFromString(stops,prefix=""):
    return [(prefix + stop.split(":")[0],stop.split(":")[1]) for stop in stops.split(";")]

