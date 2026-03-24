import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("processed_data.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.groupby("date", as_index=False).agg({"sales": "sum"})
df = df.sort_values("date")


fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Total Sales"}
)

fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("📊 Pink Morsel Sales Dashboard"),
    html.P("Sales before and after Jan 15, 2021 price increase"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)