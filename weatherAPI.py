# -*- coding: utf-8 -*-

import json, urllib2
from dbcreate import *

def accessAPI(id):
    url = "http://weather.livedoor.com/forecast/webservice/json/v1?city="
    url = url + str(id)

    response = urllib2.urlopen(url)
    jsonData = json.loads(response.read())

    print jsonData["title"].encode("utf8")
    print "発表時刻: ", jsonData["publicTime"]

    forecasts = jsonData["forecasts"]
    for forecast in forecasts:
        image = forecast["image"]
        maxTemp = forecast["temperature"]["max"]
        minTemp = forecast["temperature"]["min"]
        if maxTemp == None:
            temp = ""
        elif minTemp == None:
            temp = "(" + maxTemp["celsius"] + "/" + " )"
        else:
            temp = "(" + maxTemp["celsius"] + "/" + minTemp["celsius"] + ")"
        date = forecast["dateLabel"].encode("utf8") + "(" + forecast["date"].encode("utf8") + ")"
        weather = image["title"].encode("utf8") + " " + temp.encode("utf8")
        print date, ":", weather.strip()

    print ""
    description = jsonData["description"]
    print "天気概要(", description["publicTime"], ")"
    print description["text"].encode("utf8").replace("\n\n", "\n")

    print ""
    copyright = jsonData["copyright"]
    provider = copyright["provider"][0]
    prov = provider["name"].encode("utf8") + "(" + provider["link"].encode("utf8") + ")"
    print "配信元:", prov
    copyr = copyright["title"] + "(" + copyright["image"]["link"] + ")"
    print copyr

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "Please input the city-name."
        sys.exit(1)

    name = sys.argv[1]
    dbcreate()
    id = getCityID(name)
    accessAPI(id)

