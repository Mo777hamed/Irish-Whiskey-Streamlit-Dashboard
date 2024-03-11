import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go



df = pd.read_excel('Irish Whiskey Sales by Volume.xlsx')
df = df.dropna(subset=['Cases']) 
df['Cases'] = df['Cases'].astype(float)




year_with_most_cases = df.groupby('Year')['Cases'].sum().idxmax()
year_with_least_cases = df.groupby('Year')['Cases'].sum().idxmin()
average_cases_by_year = df.groupby('Year')['Cases'].sum().mean().__ceil__()

whiskey_quality_levels = df['Quality'].unique().tolist()
whiskey_quality_levels.insert(0, None)  

average_cases_per_year = df.groupby('Year')['Cases'].mean().reset_index()

average_cases = df.groupby('Country')['Cases'].mean().reset_index()



#Sidebar

st.sidebar.header("Irish Whiskey")
st.sidebar.image("images.jpeg")
st.sidebar.write("This Dashboard is done for Irish Whiskey Sales by Volume")
st.sidebar.write("")
st.sidebar.header('Filtering Options') 

selected_quality = st.sidebar.selectbox("Choose Quality", whiskey_quality_levels)

if selected_quality != None:
    filtered_data = df[df['Quality'] == selected_quality]
else:
    filtered_data = df

st.sidebar.write("")
st.sidebar.write("")

use_slider = st.sidebar.checkbox('Use year slider')
if use_slider:
    selected_year = st.sidebar.slider('Select a year', min_value=min(df['Year']), max_value=max(df['Year']))
    filtered_data = df[df['Year'] == selected_year]
else:
    filtered_data = df

st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("Made with :yellow_heart: by Eng. [Mohamed Ahmed](https://www.kaggle.com/mohamedelaziz)")


#Row  a

a1, a2, a3 = st.columns(3)

a1.metric("Year with Max. Cases", df.groupby('Year')['Cases'].sum().idxmax())
a2.metric("Avg. Cases by Year", "{:,}".format(average_cases_by_year) )
a3.metric("Year Min. Cases", year_with_least_cases)

st.write('')

#Row b 

st.subheader(" Irish Whiskey Quality 🍻")
fig = go.Figure(data=go.Bar(x=filtered_data['Quality'], y=filtered_data['Cases']))

st.plotly_chart(fig, use_container_width=True)



#Row c 

st.subheader(" Average Cases Over Years 📈")
fig = px.line(average_cases_per_year, x='Year', y='Cases' )

st.plotly_chart(fig)


#Row d 

st.subheader("Average Cases on World Map 🌐")
fig = px.choropleth(data_frame=average_cases,  # DataFrame containing the data
                    locations='Country',  # Column containing country names
                    locationmode='country names',
                    color='Cases',  # Column containing the values to be mapped
                    color_continuous_scale='Greys',  # Color scale for the map
                    labels={'Country': 'Country'},  # Labels for the legend
                    title='Mapping Countries')


# Add text annotations for the number of cases
fig.update_traces(text=df['Cases'],
                  hovertemplate='Country: %{location}<br>Cases: %{text}<extra></extra>')

fig.update_layout(
    mapbox=dict(
        style='carto-dark',  # Change the map style to 'carto-dark'
        zoom=1
    ),
    geo=dict(
        bgcolor='rgba(0,0,0,0)',  # Set the background color of the map to transparent
        showframe=False,
        showcoastlines=False, projection_type="natural earth"
    )
)

fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0)
)


# Add geospatial data and zoom settings for better resolution
fig.update_geos(projection_type="natural earth")
fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})

st.plotly_chart(fig)








