import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('004 happy.csv')

st.header('In search for Happiness')

data_X = st.selectbox('Select data for the X-axis',
                      ('GDP', 'Happiness', 'Generosity'))

data_Y = st.selectbox('Select data for the Y-axis',
                      ('GDP', 'Happiness', 'Generosity'))

subH = st.subheader(f"{data_X} and {data_Y}")

def fun(label):
    match label:
        case 'GDP':
            return df['gdp']
        case 'Happiness':
            return df['happiness']
        case 'Generosity':
            return df['generosity']
        case _:
            return None

x_line = fun(data_X)
y_line = fun(data_Y)

figure = px.scatter(x=x_line, y=y_line, labels={'x': data_X, 'y': data_Y}, title=f"" )

st.plotly_chart(figure)
