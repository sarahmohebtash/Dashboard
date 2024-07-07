import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children='My Dashboard'),
        dcc.Graph(
            id='My-graph',
            figure={
                 'data':[
                     {'x': [1,2,3],'y':[8,5,3],'type': 'bar', 'name': 'bar chart'},
                     {'x': [1,2,3],'y':[2,4,5],'type': 'line', 'name': 'line chart'},
                ],
                'layout': {
                     'title':'graph title',
                     'xaxis':{'title':'x axis'},
                     'yaxis':{'title':'y axis'},
                }

        })
    ])

#run
if __name__ == '__main__':
    app.run_server(debug=True)