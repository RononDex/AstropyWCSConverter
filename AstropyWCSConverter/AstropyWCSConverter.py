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