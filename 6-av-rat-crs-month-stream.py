from ssl import Options
import justpy as jp
import pandas 
from datetime import datetime
from pandas.core.dtypes.common import classes
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack()
chart_def = """
 
"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a =wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa = md")
    p1 = jp.QDiv(a=wp,text = "These graphs represent course reviews analysis " )
    

    hc = jp.HighCharts(a=wp, options = chart_def)
    hc.options.xAxis.categories=list(month_average_crs.index)
    hc_data=[{"name":v1, "data":[v2 for v2 in month_average_crs[v1]]}  for v1 in month_average_crs.columns] 
    hc.options.series = hc_data
    return wp

jp.justpy(app)
