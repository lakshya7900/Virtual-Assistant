import json

def getname():
    with open("D:\Virtual Assistant\Database\AIname.json", "r") as f:
        name = json.load(f)
        return name['name']