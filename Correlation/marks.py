import csv
import numpy as np
from numpy.core.numeric import correlate

def getDataSource(data_path):
    marks=[]
    days=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return{"x":marks,"y":days}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation-->",correlation[0,1])
def setup():
    data_path="marks.csv"
    datasource=getDataSource(data_path)
    findcorrelation(datasource)
setup()