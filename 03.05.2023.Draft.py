# In this version, the code cannot visualize any data. It suppose to draw lines but I can't figure out why it doesn't work.
# In future, I'll work on it.

import plotly.graph_objects as go
import pandas as pd

df = pd.read_excel("C:\\Users\\Ahmet\\Downloads\\video_games.xlsx")
iter = list(set(df['Metadata.Genres'].tolist()))
   

fig = go.Figure(data=
    go.Parcoords(
        # line = dict(color = df['Metrics.Used Price'],
        #            colorscale = [[0,'purple'],[0.5,'lightseagreen'],[1,'gold']]),
        line_color = "blue",
        dimensions = list([
            
            dict(range = [0, len(iter)],
                tickvals = [x for x in range(len(iter))],
                label = 'Console', values = df['Metadata.Genres'],
                ticktext = iter),

            dict(range = [df['Metrics.Used Price'].min(), df['Metrics.Used Price'].max()],
                constraintrange = [4,8],
                label = 'Price', values = df['Metrics.Used Price']),
            
            dict(range = [df['Average.Play.Time'].min(), df['Average.Play.Time'].max()],
                label = 'Play Time', values = df['Average.Play.Time']),
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
