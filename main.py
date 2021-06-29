import plotly.express as px
import csv 
import numpy as np

def plotFigure(data_path):
    with open (data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df, x="student_id", y="level", color="attempt")
        fig.show()

def getDataSource(data_path):
    studentid = []
    level = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            studentid.append(float(row["student_id"]))
            level.append(float(row["level"]))

    return {"x" : studentid, "y" : level }

def setup():
    data_path = "data.csv"
    plotFigure(data_path)

setup()
