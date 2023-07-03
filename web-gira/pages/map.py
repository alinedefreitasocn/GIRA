import streamlit as st
from legacy import legacy_session_state
from gira import preprocess
import pydeck as pdk
import pandas as pd
from datetime import time

legacy_session_state()

# processing data by station
# saving on cache?
# @st.experimental_memo
# def process_data(df):
#     # including all the preprocess steps
#     df_clean = preprocess.cleaning(df)
#     df_transform = preprocess.processing_columns(df_clean)

#     df_station = preprocess.process_all_station(df_transform)

#     df_grouped = df_station.groupby(by=['stationID',
#                                         'day_of_week',
#                                         df_station.index.hour]).agg({'numbicicletas': 'mean',
#             'station_name':'last',
#             'lat': 'last',
#             'lon': 'last'})

#     df_grouped.reset_index(inplace=True)

#     df_grouped[['stationID', 'numbicicletas']] = df_grouped[['stationID','numbicicletas']].astype(int)

#     return df_grouped


# df = groupby_(st.session_state.df)
df = pd.read_csv('/home/aline/code/personal_projects/GIRA/data/grouped_station_day_hour.csv')

day_week = st.select_slider('Day of the week',
                            options=list(df['day_of_week'].unique()))


hour = st.slider(
    "Time of the day",
    value=0,
    min_value=0,
    max_value=23)

filtered_data = df[(df['day_of_week'] == day_week) & (df['entity_ts'] == int(hour))]


st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=38.75,
        longitude=-9.14,
        zoom=11,
        pitch=50,
    ),
    # layers=[
    #     pdk.Layer(
    #         'ScatterplotLayer',
    #         data=filtered_data,
    #         get_position='[lon, lat]',
    #         get_color='[0, numbicicletas, 0]',
    #         get_radius='[numbicicletas, 0, 0]',
    #         radius_scale=10,
    #         get_fill_color='[numbicicletas, 0, 0]',
    #         pickable=True,
    #     ),
    # ],
        layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=filtered_data,
            get_position='[lon, lat]',
            get_radius='numbicicletas',
            radius_scale=30,
            pickable=True,
            opacity=0.8,
        ),
    ],
    tooltip={"text": "Number of Bicycles: {numbicicletas} \nStation: {station_name}"
             },
    map_provider="mapbox",
))
