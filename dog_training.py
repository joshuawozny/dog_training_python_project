import base64

import dash
import dash_leaflet as dl
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output
from dash import dash_table as dt
from dash import dcc
from dash import html

df = pd.read_csv("datasets/aac_shelter_outcomes.csv")
df = df.astype({"age_upon_outcome_in_weeks": "float"})

image_filename = "logo.png"  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, "rb").read())

app = Dash(__name__)

server = app.server

app.title = "Grazioso Salvare Rescue Dogs"

app.layout = html.Div(
    [
        html.Center(html.H1("Grazioso Salvare Shelter Rescue Dog Data")),
        html.Center(
            html.Img(
                width=100, src="data:image/png;base64,{}".format(encoded_image.decode())
            )
        ),
        dcc.Dropdown(
            id="dropdown-id",
            options=[
                {"label": "Water Rescue", "value": "water"},
                {"label": "Mountain Rescue", "value": "mountain"},
                {"label": "Disaster Rescue", "value": "disaster"},
                {"label": "Reset", "value": "reset"},
            ],
            value="reset",
        ),
        html.Br(),
        dt.DataTable(
            id="datatable-id",
            sort_action="native",
            sort_mode="multi",
            row_selectable="single",
            selected_columns=[],
            selected_rows=[0],
            page_action="native",
            page_current=0,
            page_size=10,
        ),
        html.H4("Designed by Joshua Wozny"),
        html.Hr(),
        # This sets up the dashboard so that your chart and your geolocation chart are side-by-side
        html.Div(
            className="row",
            style={"display": "flex"},
            children=[
                html.Div(
                    id="graph-id",
                    className="col s12 m6",
                ),
                html.Div(
                    id="map-id",
                    className="col s12 m6",
                ),
            ],
        ),
    ]
)


@dash.callback(
    Output("datatable-id", "data"),
    Output("datatable-id", "columns"),
    Input("dropdown-id", "value"),
)
def update_table(value):
    match value:
        case "water":
            myquery = (
                'animal_type == "Dog" '
                'and breed in ["Labrador Retriever Mix","Chesapeake Bay Retriever","Newfoundland",] '
                'and sex_upon_outcome == "Intact Female" '
                "and age_upon_outcome_in_weeks>=26.0 and age_upon_outcome_in_weeks<=156.0"
            )
        case "mountain":
            myquery = (
                'animal_type == "Dog" '
                'and breed in ["German Shepard","Alaskan Malamute","Old English Sheepdog",'
                '"Siberian Husky","Rottweiler",] '
                'and sex_upon_outcome == "Intact Male" '
                "and age_upon_outcome_in_weeks>=26.0 and age_upon_outcome_in_weeks<=156.0"
            )
        case "disaster":
            myquery = (
                'animal_type == "Dog" '
                'and breed in ["Doberman Pinscher","German Shepard","Golden Retriever","Bloodhound","Rottweiler",] '
                'and sex_upon_outcome == "Intact Male" '
                "and age_upon_outcome_in_weeks>=20.0 and age_upon_outcome_in_weeks<=300.0"
            )
        case _:
            myquery = 'animal_type == "Dog" '

    if myquery == "":
        data = df.to_dict("records")
        columns = [
            {"name": i, "id": i, "deletable": True, "selectable": True}
            for i in df.columns
        ]
        return data, columns
    else:
        data = df.query(myquery, inplace=False).to_dict("records")
        columns = [
            {"name": i, "id": i, "deletable": True, "selectable": True}
            for i in df.query(myquery, inplace=False).columns
        ]
        return data, columns


@app.callback(Output("graph-id", "children"), [Input("dropdown-id", "value")])
def update_graphs(value):
    ###FIX ME ####
    # add code for chart of your choice (e.g. pie chart) #
    match value:
        case "water":
            myquery = (
                'animal_type == "Dog" '
                'and breed in ["Labrador Retriever Mix","Chesapeake Bay Retriever","Newfoundland",] '
                'and sex_upon_outcome == "Intact Female" '
                "and age_upon_outcome_in_weeks>=26.0 and age_upon_outcome_in_weeks<=156.0"
            )
        case "mountain":
            myquery = (
                'animal_type == "Dog" '
                'and breed in ["German Shepard","Alaskan Malamute","Old English Sheepdog",'
                '"Siberian Husky","Rottweiler",] '
                'and sex_upon_outcome == "Intact Male" '
                "and age_upon_outcome_in_weeks>=26.0 and age_upon_outcome_in_weeks<=156.0"
            )
        case "disaster":
            myquery = (
                'animal_type == "Dog" '
                'and breed in ["Doberman Pinscher","German Shepard","Golden Retriever","Bloodhound","Rottweiler",] '
                'and sex_upon_outcome == "Intact Male" '
                "and age_upon_outcome_in_weeks>=20.0 and age_upon_outcome_in_weeks<=300.0"
            )
        case _:
            myquery = 'animal_type == "Dog" '

    if myquery == "":
        return [dcc.Graph(figure=px.histogram(data_frame=df, x="breed"))]
    else:
        return [
            dcc.Graph(
                figure=px.histogram(
                    data_frame=df.query(myquery, inplace=False), x="breed"
                )
            )
        ]


@app.callback(
    Output("map-id", "children"),
    [
        Input("datatable-id", "derived_virtual_data"),
        Input("datatable-id", "derived_virtual_selected_rows"),
    ],
)
def update_map(view_data, index):
    if view_data is None:
        return
    elif index is None:
        return

    dff = pd.DataFrame.from_dict(view_data)
    # Because we only allow single row selection, the list can be converted to a row index here
    if index is None:
        row = 0
    else:
        row = index[0]

    # Austin TX is at [30.75,-97.48]
    return [
        dl.Map(
            style={"width": "1000px", "height": "500px"},
            center=[30.75, -97.48],
            zoom=10,
            children=[
                dl.TileLayer(id="base-layer-id"),
                # Marker with tool tip and popup
                # Column 13 and 14 define the grid-coordinates for the map
                # Column 4 defines the breed for the animal
                # Column 9 defines the name of the animal
                dl.Marker(
                    position=[dff.iloc[row, 13], dff.iloc[row, 14]],
                    children=[
                        dl.Tooltip(dff.iloc[row, 4]),
                        dl.Popup(
                            [
                                html.B(html.P("Animal Name: ")),
                                html.P(dff.iloc[row, 9]),
                                html.B(html.P("Breed: ")),
                                html.P(dff.iloc[row, 4]),
                            ]
                        ),
                    ],
                ),
            ],
        )
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
