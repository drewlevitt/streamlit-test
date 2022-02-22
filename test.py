import pandas as pd
import streamlit as st
import altair as alt
from vega_datasets import data

@st.cache # Doing it this way means you only have to read the data from CSV once
def load_data(csv_path):
    return pd.read_csv(csv_path)

df = load_data('StreetLight_Sample.csv')

day_type = st.sidebar.selectbox('Day Type', ['All'] + list(df['Day Type'].unique()))
day_part = st.sidebar.selectbox('Day Part', df['Day Part'].unique())
origin = st.sidebar.multiselect('Origin Zone', df['Origin Zone Name'].unique())

st.title('My Title')

st.header('A header')

'Here is some text.'

day_type_selector = True if day_type == 'All' else (df['Day Type'] == day_type)
sub_df = df[day_type_selector & (df['Day Part'] == day_part) & df['Origin Zone Name'].isin(origin)]

sub_df

sub_df = sub_df.groupby('Destination Zone Name')['Average Daily O-D Traffic (StL Volume)'].mean().fillna(0)

st.line_chart(sub_df)

source = data.cars()

line = alt.Chart(source).mark_line().encode(
    x='Year',
    y='mean(Miles_per_Gallon)',
    color=alt.value("#FFAA00")
)

band = alt.Chart(source).mark_errorband(extent='stdev').encode(
    x='Year',
    y=alt.Y('Miles_per_Gallon', title='Miles/Gallon'),
    color=alt.value("#FFAA00")
)

line2 = alt.Chart(source).mark_line().encode(
    x='Year',
    y='mean(Displacement)',
    color=alt.value("#00AAff")
)

band + line + line2
source