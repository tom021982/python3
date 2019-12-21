
import json

pythonValue = {'car': 'Porsche', 'FastCar': True, 'Seats': 2, 'RearDoors': None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
