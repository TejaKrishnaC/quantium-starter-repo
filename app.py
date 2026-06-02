from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app=Dash(__name__)
df=pd.read_csv("formatted.csv")
df["date"]=pd.to_datetime(df["date"])
df=df.sort_values(by="date")
fig=px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Trend",
    labels={"date": "Transaction Date", "sales": "Total Sales ($)"}
)
app.layout=html.Div(children=[
    html.H1(children='Pink Morsel Visualiser',style={'textAlign':'center','color':'red'}),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )

])
if __name__ == '__main__':
    app.run(debug=True)
