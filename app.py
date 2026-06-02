from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("formatted.csv").sort_values(by="date")

app.layout = html.Div(style={'textAlign': 'center', 'fontFamily': 'Arial'}, children=[
    html.H1('Pink Morsel Visualizer', style={'color': 'gray'}),
    
    dcc.RadioItems(
        id='region-filter', 
        options=['all', 'north', 'east', 'south', 'west'], 
        value='all',
        inline=True
    ),
    
    dcc.Graph(id='sales-line-chart')
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    filtered_df = df if selected_region == 'all' else df[df['region'].str.lower() == selected_region.lower()]
    return px.line(filtered_df, x="date", y="sales", title="Sales Trend")

if __name__ == '__main__':
    app.run(debug=True)