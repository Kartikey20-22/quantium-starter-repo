import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

# Read the processed data
df = pd.read_csv('formatted_output.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Initialize the app
app = dash.Dash(__name__)

# App layout with styling
app.layout = html.Div([
    # Header
    html.H1(
        "Pink Morsel Sales Visualizer",
        style={
            'textAlign': 'center',
            'color': '#2c3e50',
            'fontFamily': 'Arial, sans-serif',
            'marginBottom': '30px',
            'paddingTop': '20px'
        }
    ),

    # Radio buttons for region filter
    html.Div([
        html.H3("Select Region:", style={'color': '#34495e', 'marginBottom': '10px'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            inline=True,
            style={
                'display': 'flex',
                'gap': '20px',
                'justifyContent': 'center',
                'marginBottom': '30px',
                'fontSize': '16px'
            },
            labelStyle={
                'cursor': 'pointer',
                'padding': '8px 16px',
                'borderRadius': '20px',
                'backgroundColor': '#ecf0f1',
                'transition': 'all 0.3s'
            }
        )
    ], style={'textAlign': 'center'}),

    # Line chart
    dcc.Graph(id='sales-chart'),

    # Key insight
    html.Div([
        html.H3("Key Insight:", style={'color': '#2c3e50'}),
        html.P(
            "The price increase on January 15, 2021 had a noticeable impact on sales.",
            style={'fontSize': '16px', 'color': '#7f8c8d'}
        )
    ], style={
        'textAlign': 'center',
        'marginTop': '30px',
        'padding': '20px',
        'backgroundColor': '#f8f9fa',
        'borderRadius': '10px',
        'margin': '30px auto',
        'maxWidth': '600px'
    })

], style={
    'maxWidth': '1200px',
    'margin': '0 auto',
    'padding': '20px',
    'backgroundColor': '#ffffff',
    'minHeight': '100vh',
    'fontFamily': 'Arial, sans-serif'
})


# Callback to update chart based on region selection
@callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data
    if selected_region == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Region'] == selected_region]

    # Aggregate by date
    daily_sales = filtered_df.groupby('Date')['Sales'].sum().reset_index()

    # Create figure
    fig = px.line(
        daily_sales,
        x='Date',
        y='Sales',
        title=f'Pink Morsel Sales - {selected_region.title()}',
        labels={'Sales': 'Total Sales ($)', 'Date': 'Date'}
    )

    # Style the chart
    fig.update_layout(
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='#ffffff',
        font={'family': 'Arial, sans-serif', 'size': 14},
        title={'x': 0.5, 'xanchor': 'center'},
        hovermode='x unified'
    )

    # Add vertical line for price increase
    fig.add_vline(
        x='2021-01-15',
        line_dash="dash",
        line_color="red",
        annotation_text="Price Increase",
        annotation_position="top"
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)