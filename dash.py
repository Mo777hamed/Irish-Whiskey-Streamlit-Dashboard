import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import plotly.express as px
import altair as alt


df = pd.read_excel('Irish Whiskey Sales by Volume.xlsx')
df = df.dropna(subset=['Cases']) 


st.write('hello')

