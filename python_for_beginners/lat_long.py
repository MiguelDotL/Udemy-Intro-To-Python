import simplekml

kml = simplekml.Kml()

def makePin(name, lon, lat, filepath, filename):
    kml.newpoint(name = name, coords = [(lon,lat)])
    if ''.join(filename[-4:]) == ".kml":
        kml.save("%(filepath)s/%(filename)s" %locals())
    else:
        kml.save("%(filepath)s/%(filename)s.kml" %locals())

# Input Prompts and Variables
nameIn      = input("Please Enter Name For New Coordinate Pair: ")
lonIn       = float(input("Enter Longitude: "))
latIn       = float(input("Enter Latitude: "))
filepathIn  = input("Where would you like to save this? [filepath]: ")
filenameIn  = input("What would you like to save the file as? [filename]: ")

makePin(nameIn, lonIn, latIn, filepathIn, filenameIn)
