import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df=pd.read_csv("data.csv")
mean = df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

graph=px.scatter(mean,x="student_id",y="level", color="attempt", size="attempt")
graph.show()