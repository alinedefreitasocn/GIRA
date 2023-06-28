import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
from gira import main
from gira import plot_map
from gira import preprocess
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="GIRA Analysis",
    page_icon="",
    layout="centered"
)

st.title('Station Analysis')

# loading the data (from where??)
@st.experimental_memo
def get_data():
    return main.init()

st.session_state.df = get_data()

# selecting the number of the station to check
stationNum = st.selectbox(
    'Station number',
    (list(st.session_state.df.stationID.unique()))) # int 64


if st.button('Generate'):
    # getting only part of df with the selected station
    station = 'station' + str(stationNum)

    # check if the station was already processed
    # if yes, used the one on session_state
    if station not in st.session_state:
        df_station = preprocess.process_station(st.session_state.df, stationNum)
        st.session_state[station] = df_station
    else:
        df_station = st.session_state[station]



    # printing the station name
    st.subheader(df_station['station_name'][0])
    # st.write(df_station.columns)


    # ploting the distribution of the time step in second
    fig = plt.figure(figsize=(10, 4))
    st.write(f'Number of missing values: {df_station["numbicicletas"].isna().sum()} out of {len(df_station["numbicicletas"])}')
    sns.lineplot(df_station.index, df_station['numbicicletas'])
    repair = df_station[df_station['estado'] == 'repair']
    # st.write(repair.columns)

    # sns.pointplot(data=repair,
    #               y='numbicicletas',
    #               linestyles=None,
    #               label='Repair')
    st.pyplot(fig)
