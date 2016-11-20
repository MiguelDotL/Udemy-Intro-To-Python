import pandas
import tkinter
from   tkinter.filedialog import askopenfilename
import simplekml

def browse():
    global fileIn
    fileIn = askopenfilename()


# def csvToKml(fileIn="./coords.csv", fileOut="./coords.kml"):
def csvToKml(fileOut="./coords.kml"):
    df  = pandas.read_csv(fileIn)
    kml = simplekml.Kml()

    for lon, lat in zip(df["Longitude"], df["Latitude"]):
        kml.newpoint(coords = [(lon,lat)])

    kml.save(fileOut)


# def csvToKml(sourcepath,sourcename, filepath, filename):
    # get filepath and filename for source .csv file
    # check if filname has .csv extension, else add extension
    # if ''.join(sourcename[-4:]) == ".csv":
    #     df  = pandas.read_csv("%(sourcepath)s/%(sourcename)s" %locals())
    # else:
    #     df  = pandas.read_csv("%(sourcepath)s/%(sourcename)s.csv" %locals())
    #
    # # parse .csv file columns with "Longitude" / "Latitude" titles
    # # zip cols together && make coord pairs
    # for lon, lat in zip(df["Longitude"], df["Latitude"]):
    #     kml.newpoint(coords = [(lon,lat)])
    #
    # # get file path for saving .kml file
    # # check if filname has .kml extension, else add extension
    # if ''.join(filename[-4:]) == ".kml":
    #     kml.save("%(filepath)s/%(filename)s" %locals())
    # else:
    #     kml.save("%(filepath)s/%(filename)s.kml" %locals())


# # Input Prompts and Variables
# sourcepathIn    = input("where is  your .csv file saved? [filepath]: ")
# sourcefileIn    = input("Which .csv file would you like to convert to .kml? [filename]: ")
# filepathIn      = input("Where would you like to save this? [filepath]: ")
# filenameIn      = input("What would you like to save the file as? [filename]: ")
#
# csvToKml(sourcepathIn, sourcefileIn, filepathIn, filenameIn)


root = tkinter.Tk()
root.title("CSV To KML Converter")

label = tkinter.Label(root, text="Some text here" )
label.pack()

browseBtn = tkinter.Button(root, text="Browse", command=browse)
browseBtn.pack()
convertBtn = tkinter.Button(root, text="Convert .csv to .kml", command=csvToKml)
convertBtn.pack()


root.mainloop()
