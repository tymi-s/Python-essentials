# python can convert data to json which is very usefull way of storing data.
import json
#converting from json to python - json.loads(content)

x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)#converts from JSON to PYTHON
print(y)# dictionary


#converting from PYTHON to JSON - json.dumps(content)

x1={"age":50,"name":"Json","surname":"coaster"}
z = json.dumps(x1)
print(type(z))

#making it eazier to read json files - adding indents and separators:
x3= {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x3))
print("\n\n\n")
print(json.dumps(x3, indent=4))
print("\n\n\n")
print(json.dumps(x3, indent=4,separators=('. '," == ")))
print("\n\n\n")
print(json.dumps(x3, indent=4,separators=('. '," == "),sort_keys=True))# sorting a content