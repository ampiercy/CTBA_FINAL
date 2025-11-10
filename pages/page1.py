from dash import html, dcc, callback, register_page, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from pathlib import Path
import us

# Register the page to page one
register_page(__name__, path="/pageone", name="Interactive Beef Trading Map")

# Load the data
data = Path(__file__).resolve().parent.parent / "data" / "beef_trading.csv"
df = pd.read_csv(data)

# Clean and Prep data
df.columns = df.columns.str.strip()
df.rename(columns={"money_spent": "Value"}, inplace=True)
df["Year"] = df["Year"].astype(int)

# Convert state names to abbreviations if needed -- AI used for this
def to_state_abbr(s):
    if not isinstance(s, str):
        return None
    s = s.strip()
    if len(s) == 2 and s.isalpha():
        return s.upper()
    st = us.states.lookup(s)
    return st.abbr if st else None

df["state_abbr"] = df["State"].apply(to_state_abbr)
df = df.dropna(subset=["state_abbr"])

# Group by year and state for the map
df_grouped = df.groupby(["Year", "state_abbr"], as_index=False)["Value"].sum()

# Layout of page one
layout = html.Div([
    html.H1("Beef Trading Value in Millions by State and Year", style={"textAlign": "center"}),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    dcc.Slider(
                        id="year-slider",
                        min=df_grouped["Year"].min(),
                        max=df_grouped["Year"].max(),
                        value=df_grouped["Year"].min(),
                        marks={str(y): str(y) for y in sorted(df_grouped["Year"].unique())},
                        step=None,
                        className="custom-slider"
                    ),
                    dcc.Graph(
                        id="choropleth-map",
                        style={"height": "600px", "width": "100%", "padding": "10px"}
                    )
                ])
            ),
            width=12
        )
    ])
], style={"padding": "10px"})

# Callback 
@callback(
    Output("choropleth-map", "figure"),
    Input("year-slider", "value")
)
def update_map(selected_year):
    d = df_grouped[df_grouped["Year"] == selected_year]

    if d.empty:
        fig = px.choropleth(locations=[""], locationmode="USA-states")
        fig.update_layout(title_text=f"No data for {selected_year}")
        return fig

    fig = px.choropleth(
        d,
        locations="state_abbr",
        locationmode="USA-states",
        scope="usa",
        color="Value",
        hover_name="state_abbr",
        hover_data={"Value": True, "state_abbr": False},
        color_continuous_scale=["#fdf0ee", "#d46a6a", "#3a0f0f"],
        labels={"Value": "Value ($)"}
    )

    fig.update_traces(hovertemplate="<b>%{location}</b><br>Value: %{z:$,.2f}<extra></extra>")

    fig.update_layout(
        title_text=f"Beef Trading Value by State ({selected_year})",
        geo=dict(bgcolor="rgba(0,0,0,0)"),
        margin={"r":0, "t":40, "l":0, "b":0}
    )

    return fig
