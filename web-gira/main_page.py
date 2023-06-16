import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
from gira import main
from gira import plot_map
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="GIRA Analysis",
    page_icon="",
    layout="centered"
)

st.title('Station Analysis')
# loading the data
@st.experimental_memo
def get_data():
    return main.init()

df = get_data()

# selecting the number of the station to check
stationNum = st.selectbox(
    'Station number',
    (list(df.stationID.unique())))
# getting only part of df with the selected station
df_station = df[df['stationID'] == stationNum]

st.session_state.df = df_station
# printing the station name
st.subheader(st.session_state.df['station_name'][0])


# setting the first value to zero as it is related to the previous station

df_station['total_seconds'][0] = 0

st.write("---")
st.write('Metrics of Time step')

c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    st.write(f"Mean: {df_station['total_seconds'].mean():.1f} s")
with c2:
    st.write(f"Median: {df_station['total_seconds'].median():.1f} s")
with c3:
    st.write(f"Min step: {df_station['total_seconds'].min():.1f} s")
with c4:
    st.write(f"Max step: {df_station['total_seconds'].max():.1f} s")
with c5:
    st.write(f"STD: {df_station['total_seconds'].std():.1f} s")

# ploting the distribution of the time step in second
fig = plt.figure(figsize=(10, 4))
sns.histplot(df_station['total_seconds'])
st.pyplot(fig)
