import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd

def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_penguin = load_lottie_url(
    'https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json'
)
st_lottie(lottie_penguin, height=1000)