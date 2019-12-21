
import re

place = '{city}'
visit = 'I visited {city} last week'
result = re.sub(place, 'Jaipur', visit)

print(result)
