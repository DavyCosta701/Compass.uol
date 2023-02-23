import json
f = open("person.json")
file = f.read()
jsonified = json.loads(file)
print(jsonified)
