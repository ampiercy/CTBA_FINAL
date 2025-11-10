import dash
from dash import html

dash.register_page(__name__, path="/")

layout = html.Div(
    className="page-content home-page",
    children=[
        # Title + Subtitle
        html.Div(
            className="page-header",
            children=[
                html.H1("Beef & Veal Trading by State 2000–2024", className="page-title"),
                html.H3("Exploring trends by state and year", className="page-subtitle"),
            ]
        ),

        # Plain description text
        html.Div(
            className="dashboard-description",
            children=[
                html.P(
                    "This dashboard explores the millions of dollars traded in beef and veal across the United States from 2000 to 2024. "
                    "The beef industry is a significant part of the U.S. economy, influencing agricultural practices, trade policies, and consumer behavior. "
                    "Understanding the patterns in beef trading can provide insights into economic trends, regional production strengths, and market demands."
                ),
                html.P(
                    "Being able to visualize this data geographically and temporally allows stakeholders to make informed decisions "
                    "regarding production, distribution, and marketing strategies. The interactive elements of this dashboard enable users to "
                    "filter and analyze the data by year or state to look for specific trends and patterns."
                ),
                html.P(
                    "Navigate through the pages to explore: "
                    "a choropleth map showing beef trading values by state for selected years, and "
                    "a line chart illustrating trends in beef trading values over time for individual states."
                ),
            ]
        ),
    ]
)