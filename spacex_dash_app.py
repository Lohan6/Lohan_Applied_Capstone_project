# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px


# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                  dcc.Dropdown(id='id', options=[
                    {'label': 'All Sites', 'value': 'ALL'},
                    {'label': 'CCAFS LC-40', 'value': 'site1'},
                    {'label': 'KSC LC-39A', 'value': 'site2'},
                    {'label': 'VAFB SLC-4E', 'value': 'site3'},
                    {'label': 'CCAFS SLC-40', 'value': 'site4'}
                ],
                value='ALL',
                placeholder="Select a Launch Site here",
                searchable=True
                ),
])
html.Br(),


@callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(entered_site):
    filtered_df = spacex_df['entered_site']
    if entered_site == 'ALL':
        fig = px.pie(data, values='class', 
        names='pie chart names', 
        title='pie chart')
        return fig
    else:
        fig = px.pie(filtered_df, values='class', 
        names='pie chart names', 
        title='pie chart')
        return fig
        # return the outcomes piechart for a selected site
html.Div(dcc.Graph(id='success-pie-chart')),
html.Br(),

html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                #dcc.RangeSlider(id='payload-slider',...)
dcc.RangeSlider(id='payload-slider',
                min=0, max=10000, step=1000,
                marks={0: '0',
                       1000: '1000'},
                value=[min_payload, max_payload]),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
html.Div(dcc.Graph(id='success-payload-scatter-chart'))

                                
@callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")])
def get_pie_chart(entered_site):
    filtered_df = spacex_df['entered_site']
    if entered_site == 'ALL':
        fig = px.scatter(data, x="Payload Mass (kg)", y="class",
        color="Booster Version Category",
        names='label names', 
        title='scatter plot')
        return fig
    else:
        fig = px.scatter(filtered_df, x="Payload Mass (kg)", y="class",
        color = "Booster Version Category",
        names='label names', 
        title='scatter plot')
        return fig
        # return the outcomes piechart for a selected site
    html.Div(dcc.Graph(id='success-pie-chart')),
html.Br(),

html.P("Payload range (Kg):"),
# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run_server()
