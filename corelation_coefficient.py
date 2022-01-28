import numpy as np
import plotly.express as px
import csv

def getDataSource(data_path):
    ice_cream_sales = []
    cold_drinks_sales = []
    with open(data_path)as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cold_drinks_sales.append(float(row["Ice-cream Sales (Rs)"]))
    return{"x":ice_cream_sales,"y":cold_drinks_sales}


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between Temperature and Ice Cream Sales = ",correlation[0,1])


def setup():
    data_path = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)


setup()