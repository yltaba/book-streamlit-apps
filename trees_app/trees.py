import streamlit as st
import pandas as pd
import numpy as np

st.title("Árvores de São Francisco")
st.write("Aplicativo para analisar árvores de São Francisco.")

trees_df = pd.read_csv('trees.csv')

st.subheader("Gráfico de linha builtin único:")

df_dbh_grouped = pd.DataFrame(trees_df.groupby('dbh', as_index=False).count()['tree_id'])
df_dbh_grouped = df_dbh_grouped.rename(columns={'tree_id':'tree_count'})
st.line_chart(df_dbh_grouped)

st.subheader("Gráfico de linha builtin com duas variáveis:")

df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500
st.line_chart(df_dbh_grouped)

st.subheader("Mapa builtin:")

trees_df_map = trees_df.dropna(subset=['longitude', 'latitude']).sample(1000)
st.map(trees_df_map)

st.subheader("Plotly:")
import plotly.express as px
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

st.subheader("Matplotlib e Seaborn:")
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

trees_df['age'] = (
    (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days
)

st.write('Seaborn')
fig_sns, ax_sns = plt.subplots()
ax_sns = sns.histplot(trees_df['age'])
plt.xlabel('Idade em dias')
st.pyplot(fig_sns)

st.write('Matplotlib')
fig_m, ax_m = plt.subplots()
ax_m = plt.hist(trees_df['age'])
plt.xlabel('Idade em dias')
st.pyplot(fig_m)


st.subheader("Bokeh:")
from bokeh.plotting import figure

scatterplot = figure(title='Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.xaxis.axis_label = 'dbh'
scatterplot.yaxis.axis_label = 'site_order'
st.bokeh_chart(scatterplot)


st.subheader("Altair:")
import altair as alt

df_caretaker = trees_df.groupby('caretaker', as_index=False)['tree_id'].count()
df_caretaker.columns = ['caretaker', 'tree_count']

fig = alt.Chart(df_caretaker).mark_bar().encode(x='caretaker', y='tree_count')
st.altair_chart(fig)

st.subheader("PyDeck:")
import pydeck as pdk

trees_df = trees_df.dropna(how='any')

sf_initial_view = pdk.ViewState(
    latitude=37.77,
    longitude=-122.4,
    zoom=11,
    pitch=45
)

# sp_layer = pdk.Layer(
#     'ScatterplotLayer',
#     data=trees_df,
#     get_position=['longitude', 'latitude'],
#     get_radius=30
# )

hx_layer = pdk.Layer(
    'HexagonLayer',
    data=trees_df,
    get_position=['longitude', 'latitude'],
    radius=100,
    extruded=True
)

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=sf_initial_view,
    layers=[hx_layer]
))