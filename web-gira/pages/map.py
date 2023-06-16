import streamlit as st
from legacy import legacy_session_state

legacy_session_state()

st.subheader(st.session_state.df['station_name'][0])
st.map(st.session_state.df[['lat', 'lon']])
