
# Assignment 9

'''
Instructions:
    
In this assignment, you will practice using the plotly express library.
https://plotly.com/python/plotly-express/

Your goal is to recreate the following graphics below using plotly express. You should
attempt to recreate them as closely as possible.

You may work individually or with a group
'''

import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = px.data.tips()

df.head()

# Bar Plot

fig = px.bar(df, x="sex", y="total_bill", color="smoker", barmode="group")

fig.show()

# Scatterplot 

fig3 = px.scatter(df, x="total_bill", y="tip", color="sex",  facet_col="smoker")
fig3.show()

fig3 = px.scatter(df, x="total_bill", y="tip", color="sex",  facet_col="smoker", trendline="ols")
fig3.show()

fig3 = px.scatter(df, x="total_bill", y="tip", facet_row="time", facet_col="day",
    category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Dinner", "Lunch"]})
fig3.show()

# Histogram

fig = px.histogram(df, x="tip", marginal="rug", hover_data=df.columns)
fig.show()

# Boxplot

fig4 = px.box(df, x="smoker", y="tip", color="smoker")
fig4.show()


