## Dictionary
countylookup = {"Alameda": "Bernalillo County", "Brazos": "Rio Arriba County", "Chimayo": "Santa Fe County"}

print countylookup["Chimayo"] ##Print third value

countylookup["Tucson"] = "Pima County" ##Add new key and value
print countylookup

print countylookup.values() ##Print all values
print countylookup.keys() ##Print all keys


