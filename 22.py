import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode





st.title('Correlations')

st.subheader("Full dataframe")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
df_cars

st.subheader("Filter dataframe on continent")
st.write("Make your choice")

df_japan = df_cars.loc[df_cars['continent']=='Japan.']
df_europe = df_cars.loc[df_cars['continent']=='Europe.']
df_us = df_cars.loc[df_cars['continent']=='US.']

button_first = st.button("Display Japan")
if button_first:
	st.write(df_japan)
button_second = st.button("Display Europe")
if button_second:
	st.write(df_europe)
button_third = st.button("Display US")
if button_third:
    st.write(df_us)

st.subheader("Heatmap")

corr_matrix = df_cars.corr()
df_corr=pd.DataFrame(corr_matrix)

viz_correlation = sns.heatmap(df_corr, cmap=sns.diverging_palette(20, 220, n=20), vmin=-1, vmax=1, annot=True)
st.pyplot(viz_correlation.figure)