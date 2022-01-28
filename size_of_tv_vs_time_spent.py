import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    size_of_tv = []
    average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spent.append(float(row["Average time spent watching TV in a week (hours)"]))

    return{"x":size_of_tv,"y":average_time_spent}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between size of tv and average time spent watching it: ",correlation[0,1])

def setup():
    data_path = "size_vs_time.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)


setup()