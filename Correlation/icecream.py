import plotly_express as px
import csv

with open("icecream.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Temperature",y="Ice-cream Sales")
    fig.show()