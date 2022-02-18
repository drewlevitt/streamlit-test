"""
# My first app
Here's our first attempt at using data to create a table:
"""

import pandas as pd
# from pyparsing import original_text_for
import streamlit as st

df = pd.read_csv('StreetLight_Sample.csv')

day_type = st.sidebar.selectbox('Day Type', df['Day Type'].unique())
day_part = st.sidebar.selectbox('Day Part', df['Day Part'].unique())
origin = st.sidebar.selectbox('Origin Zone', df['Origin Zone Name'].unique())

st.title('Streamlit 001')
'Here is some text.'
st.header('Header')
'here is some more'
st.markdown('''## Title

This is a *Markdown* block.

## Title

I have two sections with identical name. What happens now?''')

sub_df = df[(df['Day Type'] == day_type) & (df['Day Part'] == day_part) & (df['Origin Zone Name'] == origin)]

sub_df = sub_df.groupby('Destination Zone Name')['Average Daily O-D Traffic (StL Volume)'].mean().fillna(0)

# sub_df = sub_df.pivot('Day Part', 'Destination Zone Name', 'Average Daily O-D Traffic (StL Volume)').fillna(0)
# sub_df.index = range(len(sub_df))

sub_df

st.line_chart(sub_df)

# st.plotly_chart(sub_df['Destination Zone Name'], sub_df['Average Daily O-D Traffic (StL Volume)'])
# st.dataframe(df.style.highlight_max(color='blue'))
# st.dataframe(df.style.bar())