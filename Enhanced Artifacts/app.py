# app.py — CS-499 Final Project Dashboard
# Includes expanded About & Motivation section beneath author name and above search bar.

from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import dash_leaflet as dl
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import io, base64, os
from crud import AnimalShelter

matplotlib.use("Agg")

# ------------------ Database ------------------
db = AnimalShelter()

def fetch_df(q=None, limit=2000):
    try:
        data = db.read(q or {"animal_type": "Dog"})
        if limit and len(data) > limit:
            data = data[:limit]
        df = pd.DataFrame.from_records(data)
        if "_id" in df.columns:
            df = df.drop(columns=["_id"])
        return df
    except Exception as e:
        print("Database error:", e)
        return pd.DataFrame()

def query_for(filter_value):
    if filter_value == "Water":
        return {
            "$and": [
                {"$or": [
                    {"breed": {"$regex": "Labrador Retriever", "$options": "i"}},
                    {"breed": {"$regex": "Chesapeake", "$options": "i"}},
                    {"breed": {"$regex": "Newfoundland", "$options": "i"}},
                ]},
                {"sex_upon_outcome": {"$regex": "Intact Female", "$options": "i"}},
                {"age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}},
            ]
        }
    if filter_value == "Mountain":
        return {
            "$and": [
                {"$or": [
                    {"breed": {"$regex": "German Shepherd", "$options": "i"}},
                    {"breed": {"$regex": "Alaskan Malamute", "$options": "i"}},
                    {"breed": {"$regex": "Old English Sheepdog", "$options": "i"}},
                    {"breed": {"$regex": "Siberian Husky", "$options": "i"}},
                    {"breed": {"$regex": "Rottweiler", "$options": "i"}},
                ]},
                {"sex_upon_outcome": {"$regex": "Intact Male", "$options": "i"}},
                {"age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}},
            ]
        }
    if filter_value == "Disaster":
        return {
            "$and": [
                {"$or": [
                    {"breed": {"$regex": "Doberman Pinscher", "$options": "i"}},
                    {"breed": {"$regex": "German Shepherd", "$options": "i"}},
                    {"breed": {"$regex": "Golden Retriever", "$options": "i"}},
                    {"breed": {"$regex": "Bloodhound", "$options": "i"}},
                    {"breed": {"$regex": "Rottweiler", "$options": "i"}},
                ]},
                {"sex_upon_outcome": {"$regex": "Intact Male", "$options": "i"}},
                {"age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}},
            ]
        }
    return {"animal_type": "Dog"}

# ------------------ Visualization Helpers ------------------
def fig_to_base64(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=300)
    plt.close(fig)
    buf.seek(0)
    return "data:image/png;base64," + base64.b64encode(buf.read()).decode()

def make_breed_chart(df):
    if df.empty or "breed" not in df.columns:
        return html.Div("No data available.")
    vc = df["breed"].value_counts().head(10).sort_values(ascending=True)
    fig, ax = plt.subplots(figsize=(7.5, 5))
    vc.plot(kind="barh", ax=ax, color="#007acc")
    ax.set_xlabel("Count")
    ax.set_ylabel("Breed")
    ax.set_title("Top Breeds")
    ax.grid(axis="x", alpha=0.3)
    img_src = fig_to_base64(fig)
    return html.Img(src=img_src, style={"maxWidth": "100%", "height": "auto", "display": "block", "margin": "0 auto"})

# ------------------ Theme ------------------
DARK_CSS = """
body { background:#111; color:#E6E6E6; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif; }
a { color:#79b8ff; }
.card { background:#1b1b1b; border:1px solid #2a2a2a; border-radius:12px; padding:14px; }
"""

# ------------------ App ------------------
app = Dash(__name__)
server = app.server

app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        <title>CS-499 Final Project Dashboard</title>
        <style>{DARK_CSS}</style>
    </head>
    <body>
        {%app_entry%}
        <footer>{%config%}{%scripts%}{%renderer%}</footer>
    </body>
</html>
""".replace("{DARK_CSS}", DARK_CSS)

df0 = fetch_df()

logo_b64 = ""
if os.path.exists("GSL.png"):
    with open("GSL.png", "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode()

# ------------------ Layout ------------------
app.layout = html.Div([
    html.Div(
        className="card",
        style={"padding": "15px 40px", "background": "#1a1a1a", "borderRadius": "10px"},
        children=[
            # Header Row
            html.Div(
                style={"display": "flex", "alignItems": "center", "justifyContent": "space-between"},
                children=[
                    html.Img(
                        src=f"data:image/png;base64,{logo_b64}" if logo_b64 else "",
                        style={"height": "140px", "width": "140px", "objectFit": "contain", "marginRight": "20px"},
                    ),
                    html.Div(
                        style={"textAlign": "center", "flex": "1"},
                        children=[
                            html.H1("CS-499 Final Project",
                                    style={"color": "#FFFFFF", "fontSize": "2.2rem", "margin": "0"}),
                            html.H3("Created by Nicholas Wyrwas",
                                    style={"color": "#BBBBBB", "fontSize": "1.2rem", "marginTop": "6px",
                                           "fontWeight": "normal"}),
                        ],
                    ),
                    html.Div(style={"width": "140px"}),
                ],
            ),

            # About & Motivation section
            html.Div(
                style={
                    "marginTop": "25px",
                    "padding": "18px 30px",
                    "background": "#181818",
                    "borderRadius": "10px",
                    "border": "1px solid #2a2a2a",
                    "maxWidth": "80%",
                    "marginLeft": "auto",
                    "marginRight": "auto"
                },
                children=[
                    html.H2("About This Project", style={"color": "#79b8ff", "marginBottom": "10px"}),
                    html.P(
                        "This dashboard represents the culmination of my Computer Science Capstone (CS-499) at "
                        "Southern New Hampshire University. The goal was to design, build, and deploy a full-stack data "
                        "analytics solution integrating MongoDB, Python, and Dash. The application connects to a live database "
                        "from the Austin Animal Center to display real-time insights into adoption trends and rescue patterns. "
                        "It empowers users to filter and visualize data dynamically while exploring adoption outcomes "
                        "through charts and interactive mapping features.",
                        style={"fontSize": "1rem", "lineHeight": "1.7", "color": "#e0e0e0"},
                    ),
                    html.H3("Motivation", style={"color": "#79b8ff", "marginTop": "20px"}),
                    html.P(
                        "The motivation for this project stemmed from a desire to demonstrate practical application of "
                        "software engineering, database management, and data visualization in a meaningful context. "
                        "By leveraging real-world data from an animal shelter, the project showcases how technology can "
                        "support humane initiatives and improve operational efficiency. It also reflects the importance of "
                        "ethical software development and secure coding practices, which were emphasized throughout my coursework. "
                        "Ultimately, this project stands as a bridge between academic learning and real-world impact — "
                        "transforming raw data into actionable insights for decision-makers and the community.",
                        style={"fontSize": "1rem", "lineHeight": "1.7", "color": "#e0e0e0"},
                    ),
                ],
            ),

            html.Br(),

            html.H2("Search the Database",
                    style={"textAlign": "center", "color": "white", "marginTop": "10px"}),

            dcc.Input(
                id="search-text",
                placeholder="Type to search all columns...",
                type="text",
                debounce=True,
                style={
                    "width": "60%", "maxWidth": "720px", "display": "block", "margin": "0 auto",
                    "background": "#151515", "color": "#eee", "border": "1px solid #2a2a2a",
                    "borderRadius": "8px", "padding": "10px",
                },
            ),

            html.Br(),

            html.Div(
                style={"display": "flex", "justifyContent": "center", "alignItems": "center", "gap": "18px"},
                children=[
                    dcc.RadioItems(
                        id="filter_type",
                        options=[
                            {"label": " Water Rescue ", "value": "Water"},
                            {"label": " Mountain and Wilderness Rescue ", "value": "Mountain"},
                            {"label": " Disaster and Individual Rescue ", "value": "Disaster"},
                            {"label": " Reset ", "value": "Reset"},
                        ],
                        value="Reset",
                        inputStyle={"marginRight": "6px"},
                        labelStyle={"marginRight": "16px", "color": "white"},
                        style={"display": "flex", "gap": "12px"},
                    ),
                ],
            ),
        ],
    ),

    html.Br(),

    html.Div(className="card table-dark", children=[
        dash_table.DataTable(
            id="datatable-id",
            columns=[{"name": c, "id": c} for c in df0.columns] if not df0.empty else [],
            data=df0.to_dict("records"),
            style_header={"backgroundColor": "#222", "color": "#ddd"},
            style_cell={"backgroundColor": "#151515", "color": "#e6e6e6", "border": "1px solid #2a2a2a"},
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="single",
            page_action="native",
            page_current=0,
            page_size=10,
        )
    ]),

    html.Br(),

    html.Div(
        style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "16px"},
        children=[
            html.Div(className="card", id="graph-id"),
            html.Div(className="card", id="map-id"),
        ],
    ),
])

# ------------------ Callbacks ------------------
def apply_text_search(df, text):
    if not text or df.empty:
        return df
    text = str(text).strip().lower()
    mask = df.apply(lambda r: text in " ".join(map(str, r.values)).lower(), axis=1)
    return df[mask]

@app.callback(
    Output("datatable-id", "data"),
    Output("datatable-id", "columns"),
    Input("filter_type", "value"),
    Input("search-text", "value"),
)
def update_table(filter_type, search_text):
    query = query_for(filter_type)
    df = fetch_df(query)
    df = apply_text_search(df, search_text)
    cols = [{"name": c, "id": c} for c in df.columns]
    return df.to_dict("records"), cols

@app.callback(Output("graph-id", "children"), Input("datatable-id", "derived_virtual_data"))
def update_graph(virtual_data):
    df = pd.DataFrame(virtual_data or [])
    return make_breed_chart(df)

@app.callback(
    Output("map-id", "children"),
    Input("datatable-id", "derived_virtual_data"),
    Input("datatable-id", "derived_virtual_selected_rows"),
)
def update_map(virtual_data, selected_rows):
    default_center = [30.2672, -97.7431]
    df = pd.DataFrame(virtual_data or [])
    if df.empty:
        return [dl.Map(style={'width':'100%','height':'520px'}, center=default_center, zoom=10, children=[dl.TileLayer()])]
    row = 0 if not selected_rows else min(selected_rows[0], len(df)-1)
    lat = df.iloc[row].get("location_lat", None)
    lon = df.iloc[row].get("location_long", None)
    center = default_center if pd.isna(lat) or pd.isna(lon) else [float(lat), float(lon)]
    breed = str(df.iloc[row].get("breed", "Unknown"))
    name = str(df.iloc[row].get("name", "Unknown"))
    return [
        dl.Map(style={'width':'100%','height':'520px'}, center=center, zoom=12, children=[
            dl.TileLayer(),
            dl.Marker(position=center, children=[
                dl.Tooltip(breed),
                dl.Popup([html.H4("Animal"), html.Div(name)])
            ])
        ])
    ]

# ------------------ Run ------------------
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8060, debug=True)
