import requests
from bs4 import BeautifulSoup
import pendulum

def minsAway(minsAfMidLocal,timeDueStr):    
    splitTime = timeDueStr.split(":")
    minsAfMidDue = 60 * int(splitTime[0]) + int(splitTime[1])

    # Adds day to buses with late night due times.
    minsAfMidDue = minsAfMidDue + (24 * 60 * 60) if (minsAfMidDue - minsAfMidLocal) < -10 else minsAfMidDue 
    return minsAfMidDue - minsAfMidLocal

def busMinsAway(minsAfMid,dueInfo):
    if ":" in dueInfo:
        return minsAway(minsAfMid,dueInfo)
    
    if "Due" in dueInfo:
        return 0

    return int(dueInfo[:-5])

URL = "http://yorkshire.acisconnect.com/Text/WebDisplay.aspx?stopRef={}"
def getInfoFromID(stop,routes):
    result = requests.get(URL.format(stop[1]))
    doc = BeautifulSoup(result.text,"html.parser")

    try:
        rows = (doc.table.find_all("tr"))
    except:
     rows = []

    buses = []
    if len(rows) != 0:
        rows = rows[1:]
        for row in rows:
            temp = row.find_all("td")
            temp = [td.text for td in temp][:-1]
            temp.insert(0,stop[0])
            if temp[1].upper() in routes or len(routes) == 0 or (len(routes) == 1 and routes[0] == ""):
                buses.append(temp)

    return buses

def getAllInfo(stops,routes):
    buses = []
    for stop in stops:
        buses.extend(getInfoFromID(stop,routes))
    localTime = pendulum.now("Europe/London")
    minsAfMidLocal  = localTime.hour * 60 + localTime.minute
    return sorted(buses, key=lambda x:busMinsAway(minsAfMidLocal,x[3]))

STAND_BASE_ID = 45030219
def allCoachStnStops():
    stops = []
    for stand in range(4,23):
        stops.append(("Stand " + str(stand),STAND_BASE_ID + stand))
    return stops


if __name__ == "__main__":
    
    stops = []
    stops = allCoachStnStops()

    buses = getAllInfo(stops)
        
    for bus in buses:
        print(bus)
