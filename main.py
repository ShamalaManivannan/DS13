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

top12_uni = pd.DataFrame(data.groupby('State')['Score'].sum().nlargest(12).sort_values(ascending = True))

fig1 = go.Figure()

fig1.add_trace(go.Scatter(x= top12_uni.index, y=top12_uni["Score"], fill = 'tonexty', line_color = 'red'))
fig1.update_layout(title = "Top 10 University States by score")
fig1.write_html("Fig1.html",auto_open = True)

top12_unirank = pd.DataFrame(data.groupby("State")['Score'].sum().nlargest(12).sort_values(ascending = True))

fig2  = px.scatter(top12_unirank, x = top12_unirank.index, y = 'Score', size = 'Score', size_max = 120, color = top12_unirank.index, title = "Top 12 University States by score ")
fig2.write_html('Fig2.html', auto_open = True) 

top12_unirankname = pd.DataFrame(data.groupby("Name")['Rank'].sum().nsmallest(12).sort_values(ascending = False))

fig3  = px.scatter(top12_unirankname, x = top12_unirankname.index, y = 'Rank', size = 'Rank', size_max = 120, color = top12_unirankname.index, title = "Top 12 Universities by Rank ")
fig3.write_html('Fig3.html', auto_open = True) 

top12_unicity = pd.DataFrame(data.groupby("City")['Score'].sum().nlargest(12).sort_values(ascending = True))

fig4  = px.scatter(top12_unicity, x = top12_unicity.index, y = 'Score', size = 'Score', size_max = 120, color = top12_unicity.index, title = "Top 12 University Cities by Score ")
fig4.write_html('Fig4.html', auto_open = True)