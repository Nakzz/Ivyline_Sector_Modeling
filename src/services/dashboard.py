from distutils.log import debug
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


class Dashboard():

    def headline(self):

        return [html.H1(children='JJ&J Investment: Sector & Equity Modeling-Pitch Challenge'),
                html.Div(children='''
            '''),
                dcc.Markdown(children='''
            ### AJ Naqib, João Carvalhais, Jacob Fox
            [Ivyline Capital](https://www.linkedin.com/company/ivylinecapitalgroup/)
            
            Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
            if this is your first introduction to Markdown!
''')]

    def demo_fig(self):
        fig = px.bar(self.data, x="Ticker", y="Market Cap")

        return [dcc.Graph(
            id='example-graph',
            figure=fig
        )]

    def demo_generate_table(self, max_rows=10):
        dataframe = self.data
        return html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in dataframe.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                ]) for i in range(min(len(dataframe), max_rows))
            ])
        ])

    def demo_scatter_plot(self):
        fig = px.scatter(self.data, x="ROIC", y="P/E",
                         size="Market Cap", color="Ticker", hover_name="Name",
                         log_x=True, size_max=60)

        return dcc.Graph(
            figure=fig
        )

    def setup_layout(self):

        self.app.layout = html.Div(
            # style={'backgroundColor': colors['background']},
            children=[
                *self.headline(),
                *self.demo_fig(),
                self.demo_generate_table(),
                self.demo_scatter_plot()

            ])

    def __init__(self, data):
        self.app = Dash(__name__)
        self.data = data
        self.setup_layout()

    def run(self):
        self.app.run_server(debug=True, port=5002)


colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
