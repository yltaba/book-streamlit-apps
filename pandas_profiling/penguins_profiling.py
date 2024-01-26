import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_lottie import st_lottie
# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_penguin = load_lottie_url(
    'https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json'
)
st_lottie(lottie_penguin, height=1000, width=800)

st.title("Palmer's Penguins")
selected_x_var = st.selectbox('What do want the x variable to be?', 
                              ['bill_length_mm', 'bill_depth_mm', 
                               'flipper_length_mm', 'body_mass_g']) 

selected_y_var = st.selectbox('What about the y?', 
                              ['bill_depth_mm', 'bill_length_mm', 
                               'flipper_length_mm', 'body_mass_g']) 

penguin_file = st.file_uploader('Select Your Local Penguins CSV')

if penguin_file:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')

sns.set_style('darkgrid')
markers = {
    'Adelie':'X',
    'Gentoo':'s',
    'Chinstrap':'o'
}

fig, ax = plt.subplots()
ax = sns.scatterplot(data=penguins_df,
                     x=selected_x_var,
                     y=selected_y_var,
                     hue='species',
                     markers=markers,
                     style='species')
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplor of Palmer's Penguins")
st.pyplot(fig)

# st.title('Pandas Profiling on this Data:')
# penguin_profile = ProfileReport(penguins_df, explorative=True)
# st_profile_report(penguin_profile)
