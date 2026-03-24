import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("processed_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

# 🎨 Layout with styling
app.layout = html.Div(
    style={"backgroundColor": "#f5f7fa", "padding": "20px"},
    children=[

        html.H1(
            "📊 Pink Morsel Sales Dashboard",
            style={"textAlign": "center", "color": "#2c3e50"}
        ),

        html.P(
            "Analyse sales before and after Jan 15, 2021 price increase",
            style={"textAlign": "center", "color": "#555"}
        ),

        # 🔘 Radio buttons
        html.Div([
            html.Label("Select Region:", style={"fontWeight": "bold"}),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "South", "value": "south"},
                    {"label": "East", "value": "east"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True
            )
        ], style={"textAlign": "center", "margin": "20px"}),

        # 📊 Graph
        dcc.Graph(id="sales-graph")
    ]
)

@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[
            filtered_df["Region"].str.lower() == selected_region
        ]

    # 🔥 FIX: group properly
    filtered_df = (
        filtered_df.groupby("Date", as_index=False)
        .agg({"Sales": "sum"})
        .sort_values("Date")
    )

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title="Sales Over Time",
        labels={"Date": "Date", "Sales": "Total Sales"}
    )

    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)