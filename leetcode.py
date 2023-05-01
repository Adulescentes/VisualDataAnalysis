
import json

with open("csvjson.json", "r") as f:
    data = json.load(f)


newList = []

remain = [5, 5, 5, 5, 5]

for element in data:

    if element["Release.Console"] == "Nintendo DS" and remain[0] > 0:
        newList.append(element)
        remain[0] -= 1
    elif element["Release.Console"] == "Sony PSP" and remain[1] > 0:
        newList.append(element)
        remain[1] -= 1
    elif element["Release.Console"] == "X360" and remain[2] > 0:
        newList.append(element)
        remain[2] -= 1
    elif element["Release.Console"] == "PlayStation 3" and remain[3] > 0:
        newList.append(element)
        remain[3] -= 1
    elif element["Release.Console"] == "Nintendo Wii" and remain[4] > 0:
        newList.append(element)
        remain[4] -= 1

    if len(newList) == 25:
        break


# points = data[0]["Metrics.Review Score"]

# console = data[0]["Release.Console"]

newList.sort(key= lambda x: x["Metrics.Review Score"])

with open("result.json", "w+") as f:
    json.dump(newList, f, indent=4)

