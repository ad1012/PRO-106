import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='Coffee In ml', y='sleep in hours')
        fig.show()

def getDataSource(data_path):
    cups_of_coffee = []
    sleep_in_hours = []
    
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep_in_hours.append(float(row["sleep in hours"]))
            cups_of_coffee.append(float(row["Coffee in ml"]))
            
            
    return {"x" : sleep_in_hours, "y" : cups_of_coffee }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Cups of Coffee vs Hours of Sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
