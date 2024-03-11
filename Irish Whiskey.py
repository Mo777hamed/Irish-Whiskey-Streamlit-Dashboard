import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import plotly.express as px
import altair as alt


df = pd.read_excel('https://query.data.world/s/uhu2eebycbrrewyxffus4wpjcbb7ap?dws=00000')
df = df.dropna(subset=['Cases']) 


st.write('hello')

