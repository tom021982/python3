
# Avoid passing mutable data containers as args to a function. Consistency is compromised.

countries = ["India", "Germany", "France"]

def revisecountries(countries):
    countries.extend(["UK", "USA", "Denmark"])     # content changed
    # print(countries)
    return countries

newcountries = revisecountries(countries)
print(countries)
print(newcountries)    # changed container - inconsistent
