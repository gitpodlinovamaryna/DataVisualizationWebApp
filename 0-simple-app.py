import justpy as jp
from pandas.core.dtypes.common import classes

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a = wp, text = "Analysis of Course Reviews", classes = "text-h3 text-center q-pa=md")
    p1 = jp.QDiv(a =wp, text = "These graphs represent course reviews analysis ")
    return wp

jp.justpy(app)
