import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Temperature", y="Ice-cream Sales( â‚¹ )")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    cups_of_coffee = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Temperature"]))
            cups_of_coffee.append(float(row["Ice-cream Sales( â‚¹ )"]))

    return {"x" : ice_cream_sales, "y": cups_of_coffee}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream Sales :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"

    #datasource = getDataSource(data_path)
    #findCorrelation(datasource)
    #plotFigure(data_path)

setup()