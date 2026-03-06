import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Gap Minder Dashboard")
df = pd.read_csv('gapminder_data_graphs.csv')

uniqueYear = df['year'].unique()
selectedYear = st.selectbox("Select the Year", uniqueYear)
dfSelectedYear = df[df['year'] == selectedYear]
averageGDP = round(dfSelectedYear["gdp"].mean(), 2)
averageLifeExp = round(dfSelectedYear["life_exp"].mean(), 2)
averageHdi = round(dfSelectedYear["hdi_index"].mean(), 2)
c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Average GDP :", averageGDP)
with c2:
    st.metric("Average Life Expectancy :", averageLifeExp)
with c3:
    st.metric("Average HDI:", averageHdi)

scatterPlot = px.scatter(
data_frame=dfSelectedYear,
    x='gdp',
    y='life_exp',
    color='continent',
    title = f"Scatter Plot for year {selectedYear} you can see below "
)
st.plotly_chart(scatterPlot)

c4,c5 = st.columns(2)
with c4:
    histogram1 = px.histogram(
        data_frame=dfSelectedYear,
        x = 'continent',
        y='gdp',
        title = "Distribution of GDP accross differnt continent"
    )
    st.plotly_chart(histogram1)
    st.histogram(
        data=dfSelectedYear,
        x = "continent",
        y='gdp'
    )