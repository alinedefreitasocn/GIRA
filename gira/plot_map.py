import pandas as pd
import plotly.express as px
import plotly.io as pio

# pio.renderers.default = "browser"

def scatter(df:pd.DataFrame):
    # buble map with animation from plotly

    fig = px.scatter_geo(data_frame=df,
                        lat='lat',
                        lon='lon',
                        color="numbicicletas",
                        hover_name="stationID", #size="numbicicletas",
                        animation_frame=df.index,
                        projection="natural earth",
                        #scope='europe'
                        )
    fig.update_layout(lonaxis = dict(
            showgrid = True,
            gridwidth = 0.5,
            range= [ -9.301437, -8.954681],
            dtick = 5
        ),
        lataxis = dict(
            showgrid = True,
            gridwidth = 0.5,
            range= [ 38.676979, 38.808727 ],
            dtick = 5
        )
    )

    fig.show()
