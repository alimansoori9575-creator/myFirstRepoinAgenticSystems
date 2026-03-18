###         Interactive Training Visualization using Plotly         ###
import pandas as pd
import plotly.express as px

df = DataFrame = ({
    "epoch" : range(1,11),
    "loss": [0.9,0.8,0.7,0.6,0.5,0.4,0.45,0.3,0.7,0.35]
})

fig = px.line(
    df,
    x= "epoch",
    y= "loss",
    title= "Loss vs Epoch"
)


fig.add_annotation(
    x= 6,
    y= 0.4,
    text='From here Loss unstabalise',
    showarrow=True,
    arrowhead=6
)

fig.show()