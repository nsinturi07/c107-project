import pandas as pd
import csv
import plotly.graph_objects as go
df=pd.read_csv("data")
student_df=df.loc[df["student_id"]=="TRL_rst"]
print(df.groupby("level")["attempt"].mean())
graph=go.Figure(go.Bar(
    x=["level1","level2","level3","level4"],
    y=df.groupby("level")["attempt"].mean(),
    orientation="v"
))
graph.show()