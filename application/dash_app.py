import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def init_dash(server):

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    dash_app = dash.Dash(server=server, 
        external_stylesheets=external_stylesheets,
        routes_pathname_prefix='/dashapp/'
    )

    dash_app.layout = html.Div([
        html.H6("Change the value in the text box to see callbacks in action!"),
        html.Div(["Input: ",
                dcc.Input(id='my-input', value='initial value', type='text')]),
        html.Br(),
        html.Div(id='my-output'),

    ])


    @dash_app.callback(
        Output(component_id='my-output', component_property='children'),
        Input(component_id='my-input', component_property='value')
    )
    def update_output_div(input_value):
        return 'Output: {}'.format(input_value)

    # server = dash_app.server
    return dash_app.server
# if __name__ == "__main__":
#     app.run_server(debug=True, host="0.0.0.0")
