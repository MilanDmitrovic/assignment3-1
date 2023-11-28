someNumber = 10

# Proveravamo da li someNumber ima vrednost veću od nule
if someNumber > 0:
    print("Above zero")
# Ako prvi uslov nije ispunjen, proveravamo da li someNumber ima vrednost manju od nule
elif someNumber < 0:
    print("Below zero")
# Ako ni jedan od prethodnih uslova nije ispunjen, ispisujemo "Zero"
else:
    print("Zero")
