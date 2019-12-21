
import shelve
s = shelve.open("CityList")

s["India"] = "Delhi"
s["Russia"] = "Moscow"
s["Thailand"] = "Bangkok"

for key in s:
    print(key)

s.close()
