import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import plotly
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("nirf_university_rankings.csv")

data.columns = ['Institute ID','Name','City','State','Score','Rank']

data.fillna(value = "?", inplace = True)

print(data.info())
print(data.head())

top12_uni = pd.DataFrame(data.groupby('State')['Score'].sum().nlargest(10).sort_values(ascending = True))

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x= top12_uni.index, y=data["Score"], fill = 'tonexty', line_color = 'red'))
fig1.update_layout(title = "Top 10 Universities by score")
fig1.write_html("Fig1.html",auto_open = True)