import simplekml

kml = simplekml.Kml()

def makePin(name, lat, lon, filepath, filename):
    kml.newpoint(name = name, coords = [(lat,lon)])
    if ''.join(filename[-4:]) == ".kml":
        kml.save("%(filepath)s/%(filename)s" %locals())
    else:
        kml.save("%(filepath)s/%(filename)s.kml" %locals())

# Input Prompts and Variables
nameIn      = input("Please Enter Name For New Coordinate Pair: ")
latIn       = float(input("Enter Latitude: "))
lonIn       = float(input("Enter Longitude: "))
filepathIn  = input("Where would you like to save this? [filepath]: ")
filenameIn  = input("What would you like to save the file as? [filename]: ")

makePin(nameIn, latIn, lonIn, filepathIn, filenameIn)
