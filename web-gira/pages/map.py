import streamlit as st
from legacy import legacy_session_state
from gira import preprocess
import pydeck as pdk

legacy_session_state()

# processing data by station
# saving on cache?
@st.experimental_memo
def process_data(df):
    # including all the preprocess steps
    df_clean = preprocess.cleaning(df)
    df_transform = preprocess.processing_columns(df_clean)

    df_station = preprocess.process_all_station(df_transform)

    df_grouped = df_station.groupby(by=['stationID',
                                        'day_of_week',
                                        df_station.index.hour])/
    .agg({'numbicicletas': 'mean',
            'station_name':'last',
            'lat': 'last',
            'lon': 'last'})

    df_grouped.reset_index(inplace=True)

    df_grouped[['stationID', 'numbicicletas']] = df_grouped[['stationID','numbicicletas']].astype(int)

    return df_grouped


df = groupby_(st.session_state.df)

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=38.75,
        longitude=-9.14,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color='numbicicletas',
            get_radius=200,
        ),
    ],
))
