import json
from datetime import datetime


def createhistory(methodname, data):
    try:
        with open('proverka.json', 'r') as read_json:
            history = json.load(read_json)
    except FileNotFoundError:
            history = {}
            history["Prima"] = []
            history["Daykstra"] = []
            history["Floyda"] = []
            history["Kraskala"] = []
    except:
        return "Unknown error"
    
    current_day = datetime.now()
    string = current_day.strftime('%Y-%m-%d %H:%M:%S')
    if(methodname == "Prima"):
        history["Prima"].append({"date":string, "edge_list":data[0], "mst":data[1]})
    elif(methodname == "Kraskala"):
        history["Kraskala"].append({"date":string, "edge_list":data[0], "mst":data[1]})
    elif(methodname == "Floyda"):
        history["Floyda"].append({"date":string, "original":data[0], "result":data[1]})
    elif(methodname == "Daykstra"):
        history["Daykstra"].append({"date":string, "original":data[0], "result":data[1]})
        
    with open('proverka.json', 'w') as outfile:
        json.dump(history, outfile, indent = 3)
        

