import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Read the processed data
df = pd.read_csv('formatted_output.csv')

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by date
df = df.sort_values('Date')

# Aggregate sales by date (sum all regions)
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Create the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    # Header
    html.H1("Pink Morsel Sales Visualizer", style={'textAlign': 'center'}),

    # Line chart
    dcc.Graph(
        id='sales-chart',
        figure=px.line(
            daily_sales,
            x='Date',
            y='Sales',
            title='Pink Morsel Sales Over Time',
            labels={'Sales': 'Total Sales ($)', 'Date': 'Date'}
        )
    ),

    # Answer to the question
    html.Div([
        html.H3("Key Insight:"),
        html.P("The price increase on January 15, 2021 had a noticeable impact on sales.")
    ], style={'textAlign': 'center', 'marginTop': '20px'})
])

if __name__ == '__main__':
    app.run(debug=True)