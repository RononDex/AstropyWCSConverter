#   This script transforms RA/DEC coordinates from an input csv file "WCS_Transform.csv"
#   to local x/y coordinates on a 2D plane / picture using a wcs.fits file 
#   The wcs.fits file contains the transformation matrices used to transform the coordinates
#   The transformation is SIP compatible, meaning it also includes optical distortions from telescope optics

#   Input CSV file should look like this:
#       [obj_name];[RA];[DEC]
#   Ouput CSV file will look like this:
#       [obj_name];[RA];[DEC];[X];[Y]

from astropy.wcs import WCS
import numpy as np
import csv

w = WCS('wcs.fits')
print(w.wcs.name)
newCsv = "";
with open('WCS_Transform.csv', 'r') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in csvReader:
        px, py = w.wcs_world2pix(float(row[1]), float(row[2]), 1)
        print("Transformed RA", row[1], " and DEC", row[2], " to X", px, " and Y", py)
        newCsv = newCsv + str(row[0]) + ";" + str(row[1]) + ";" + str(row[2]) + ";" + str(px) + ";" + str(py) + "\n"

f = open("WCS_Transform_Output.csv","w") 
f.write(newCsv)
f.close()