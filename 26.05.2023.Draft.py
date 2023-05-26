import plotly.graph_objects as go
import pandas as pd

if 1:
    df = pd.read_excel("C:\\Users\\Ahmet\\Downloads\\video_games.xlsx")
else:
    df = pd.read_csv("csvjson.csv")


"""
1- Oyuncuların en yüksek puan verdikleri oyun türü nedir ve bu türdeki oyunlar hangi platformlarda yayınlanmıştır?

2- Oyunların en çok tercih edilen yayıncıları kimlerdir ve bu yayıncılar hangi türdeki oyunları yayınlamaktadır?

3- Hangi yıl en fazla oyun yayınlandı ve o yılki en popüler olan oyun türü nedir?
"""
# Puan          -- Metrics.Review Score
# Oyun Türü     -- Metadata.Genres
# Platform      -- Release.Console
# Yayımcı       -- Metadata.Publishers
# Yıl           -- Release.Year

#
#   Mouse Hover ile oyunla alakalı öne çıkarma yap
#

# Motivasyon - Giriş
    # Neden paralel koordinat kullanıyorum?
    # Geçmişte yapılan çalışmalara atıf
    # Veri görselleştirmenin önemi

# Görsellerin tanıtımları
    # İnternetteki araçların ürettiği görseller + benim kodumun çıktıları
    # ve kodlar ve açıklamaları

# Projeyi geliştirirken karşılaştığım sorunlar ve çözümlerim

# Projeyi daha sonra geliştirmek istersem neler yapabilirim?

gameType = df['Metadata.Genres'].tolist()


gameTypeSet = {}
num = 0
for i in gameType:
    if i not in list(gameTypeSet.keys()):
        gameTypeSet[i] = num
        num += 1

gameTypeValues = df['Metadata.Genres']
gameTypeValues = gameTypeValues.replace(gameTypeSet)


console = df["Release.Console"].tolist()
consoleSet = {}
num = 0
for i in console:
    if i not in list(consoleSet.keys()):
        consoleSet[i] = num
        num += 1

consoleValues = df["Release.Console"]
consoleValues = consoleValues.replace(consoleSet)

fig = go.Figure(data=
    go.Parcoords(
        line = dict(color = [x for x in range(len(gameType))],
                   colorscale = [[0,'purple'],[0.5,'lightseagreen'],[1,'gold']]),
        # line_color = "blue",
        dimensions = list([
            
            dict(range= [df["Metrics.Review Score"].min(), df['Metrics.Review Score'].max()],
                 label = "Score",
                 values = df['Metrics.Review Score'].tolist()
            ),
            
            dict(
                tickvals = [x for x in range(len(list(gameTypeSet.keys())))],
                label = 'Game Type', 
                values = gameTypeValues,
                ticktext = list(gameTypeSet.keys())
                ),

            dict(
                tickvals = [x for x in range(len(list(consoleSet.keys())))],
                label = "Console",
                values = consoleValues,
                ticktext = list(consoleSet.keys())
                )
        ])
    )
)

fig.update_layout(
    plot_bgcolor = 'white',
    paper_bgcolor = 'white'
)

fig.show()