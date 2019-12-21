
import json

stringOfJsonData = '{"car": "Porsche", "FastCar": true, "Seats": 2, "RearDoors": null}'

JsonAsPythonValue = json.loads(stringOfJsonData)
print(JsonAsPythonValue)
