# -*- coding: utf-8 -*-
import json, urllib2

url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=040010"

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

