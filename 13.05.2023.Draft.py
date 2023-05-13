import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel("C:\\Users\\Ahmet\\Downloads\\video_games.xlsx")
iter = list(set(df['Metadata.Genres'].tolist()))

fig = go.Figure(data=
    go.Parcoords(
        line = dict(color = [x for x in range(len(iter))],
                   colorscale = [[0,'purple'],[0.5,'lightseagreen'],[1,'gold']]),
        # line_color = "blue",
        dimensions = list([
            
            dict(range = [0, len(iter)],
                tickvals = [x for x in range(len(iter))],
                label = 'Console', 
                values = [x for x in range(len(iter))],
                ticktext = iter),

            dict(range = [df['Metrics.Used Price'].min(), df['Metrics.Used Price'].max()],
                label = 'Price', 
                values = df['Metrics.Used Price']),
            
            dict(range = [df['Average.Play.Time'].min(), df['Average.Play.Time'].max()],
                label = 'Play Time', 
                values = df['Average.Play.Time']),

            # dict(range = [0,8],
            #     label = 'Petal Width', values = df['petal_width'])
        ])
    )
)

fig.update_layout(
    plot_bgcolor = 'white',
    paper_bgcolor = 'white'
)

fig.show()
