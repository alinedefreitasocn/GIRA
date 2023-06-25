import streamlit as st
from legacy import legacy_session_state
from gira import preprocess
import pydeck as pdk

legacy_session_state()

# processing data by station
# saving on cache?
@st.experimental_memo
def process():
    return preprocess.process_all_station(st.session_state.df)

df_processed = process()

st.subheader('Bicicle Distribution')

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
            data=df_processed,
            get_position='[lon, lat]',
            get_color='numbicicletas',
            get_radius=200,
        ),
    ],
))
