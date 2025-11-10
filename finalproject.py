# AI Usage:
# ChatGPT was used to generate ideas for the dashboard and help clarify code,
# change formatting in graphs, and find specifc colors to match the theme of 
# beef trading and ensure the colors used were colorblind friendly. ChatGPT 
# helped a lot with state abbreviation conversion in page 1 to ensure that the 
# choropleth map would render correctly. Also used to help with certain packages
# such as us for state abbreviation lookup. I also used it to help with how to 
# implement the app into a web link through Render by connecting it to GitHub.
# Copilot was used for some code completion suggestions and to fix some of the code
# when there were errors. It also gave me some ideas for how to format a few of my pages.
# Both tools were used to help debug errors in the code during development and the design
# file to ensure it was visually appealing. Some help with the layout and the functions of 
# the dropdowns and sliders. 

import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    title="Andrew Piercy Makeup Final Dashboard",
)
server = app.server

app.layout = html.Div(
    className="page-wrapper",
    children=[
        # Navbar
        dbc.Navbar(
            dbc.Container([
                dbc.NavbarBrand("Andrew Piercy Makeup Final Dashboard", className="brand-text"),

                # Centered nav links
                dbc.Nav(
                    [
                        dbc.NavLink("Home", href="/", active="exact"),
                        dbc.NavLink("Interactive Beef Trading Map", href="/pageone", active="exact"),
                        dbc.NavLink("Beef Trade Time Series", href="/pagetwo", active="exact"),
                    ],
                    className="nav-links"
                ),
            ], fluid=True),
            className="custom-navbar",
            dark=True
        ),

        # Page content container
        html.Div(dash.page_container, className="page-content"),

        # Footer
        html.Footer(
            "Andrew Piercy Makeup Dash - Data from USDA Economic Research Service",
            className="footer"
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True) 
