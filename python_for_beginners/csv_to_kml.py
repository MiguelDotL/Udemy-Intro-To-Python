import pandas
import simplekml

kml = simplekml.Kml()

def csvToKml(sourcepath,sourcename, filepath, filename):
    # get filepath and filename for source .csv file
    # check if filname has .csv extension, else add extension
    if ''.join(sourcename[-4:]) == ".csv":
        df  = pandas.read_csv("%(sourcepath)s/%(sourcename)s" %locals())
    else:
        df  = pandas.read_csv("%(sourcepath)s/%(sourcename)s.csv" %locals())

    # parse .csv file columns with "Longitude" / "Latitude" titles
    for lon, lat in zip(df["Longitude"], df["Latitude"]):
        kml.newpoint(coords = [(lon,lat)])

    # get file path for saving .kml file
    # check if filname has .kml extension, else add extension
    if ''.join(filename[-4:]) == ".kml":
        kml.save("%(filepath)s/%(filename)s" %locals())
    else:
        kml.save("%(filepath)s/%(filename)s.kml" %locals())


# Input Prompts and Variables
sourcepathIn    = input("where is  your .csv file saved? [filepath]: ")
sourcefileIn    = input("Which .csv file would you like to convert to .kml? [filename]: ")
filepathIn      = input("Where would you like to save this? [filepath]: ")
filenameIn      = input("What would you like to save the file as? [filename]: ")

csvToKml(sourcepathIn, sourcefileIn, filepathIn, filenameIn)
