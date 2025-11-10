import dash
from dash import html, dcc, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
from pathlib import Path

#register page 2
register_page(__name__, path="/pagetwo", name="Beef Trade Time Series")

# Load Data
DataPath_beef = Path(__file__).resolve().parent.parent / "data" / "beef_trading.csv"
beef = pd.read_csv(DataPath_beef)

# Clean Data
beef = beef[beef["Commodity"] == "Beef and veal"]
beef["Year"] = beef["Year"].astype(int)
beef.sort_values(["State", "Year"], inplace=True)

# Layout of Page 2
layout = html.Div([
    html.H1("Beef and Veal Trade Value in Millions by State", style={"textAlign": "center", "marginBottom": "20px"}),

    html.Div(className="card", children=[
        html.Label("Select a State:"),
        dcc.Dropdown(
            id="state-selector",
            options=[{"label": state, "value": state} for state in sorted(beef["State"].unique())],
            value="California",
            clearable=False,
        ),
    ], style={"marginBottom": "20px"}),

    html.Div(className="card", children=[
        dcc.Graph(id="beef-trend-graph"),
        html.P("Hover over the line to see yearly trade values.", style={
            "color": "#7a8a80", "fontStyle": "italic", "marginTop": "10px", "textAlign": "left"
        }),
    ]),
])

# Callback 
@callback(
    Output("beef-trend-graph", "figure"),
    Input("state-selector", "value"),
)
def update_beef_chart(selected_state):
    state_data = beef[beef["State"] == selected_state]
    fig = px.line(
        state_data,
        x="Year",
        y="Value",
        labels={"Year": "Year", "Value": "Trade Value (Million $)"},
        title=f"Beef and Veal Trade Value in {selected_state}",
        markers=True,
        color_discrete_sequence=["#d46a6a"],
    )
    fig.update_layout(
        xaxis=dict(tickmode="linear", dtick=1),
        plot_bgcolor="#f5f7f4",
        paper_bgcolor="#ffffff",
        hovermode="x unified",
    )
    return fig