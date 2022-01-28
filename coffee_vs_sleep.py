import csv
from msilib.schema import File
import plotly.express as px

with open("cups of coffee vs hours of sleep.csv") as csv_File:
    df = csv.DictReader(csv_File)
    fig = px.scatter(df,x = "Coffee in ml", y = "sleep in hours")
    fig.show()