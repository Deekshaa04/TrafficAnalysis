import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

import base64
from PIL import Image
# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Path to your local image
image_path = "./pngtree-technology-data-line-dotted-line-picture-image_931862.jpg"

# Get base64 encoded image
encoded_image = image_to_base64(image_path)

# Inject custom CSS with the base64 image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        
    }}
     
    </style>
    """,
    unsafe_allow_html=True
)
# Load the dataset

data_path = './transformed_data.csv'  # Update with your actual file path if different
df = pd.read_csv(data_path)
st.markdown(
    """
    <h1 style="color: #FF6347;">Traffic Congestion Analysis</h1>
    """,
    unsafe_allow_html=True
)
# Convert timestamp to datetime and extract hour and day of week
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour

# Part 1: Hourly Traffic Analysis (Line Plot)

# Group by hour to analyze average vehicle count and average speed
hourly_traffic = df.groupby('hour').agg({
    'vehicle_count': 'mean', 
    'average_speed': 'mean'
}).reset_index()

# Create a Plotly line plot for 'vehicle_count' and 'average_speed' by 'hour'
fig_hourly = go.Figure()

# Add line for Vehicle Count
fig_hourly.add_trace(go.Scatter(
    x=hourly_traffic['hour'], 
    y=hourly_traffic['vehicle_count'],
    mode='lines', 
    name='Vehicle Count'
))

# Add line for Average Speed
fig_hourly.add_trace(go.Scatter(
    x=hourly_traffic['hour'], 
    y=hourly_traffic['average_speed'],
    mode='lines', 
    name='Average Speed',
    line=dict(color='orange')
))

# Update layout with title, labels, and grid for hourly analysis
fig_hourly.update_layout(
    title='Traffic Volume and Speed by Hour',
    xaxis_title='Hour of the Day',
    yaxis_title='Count / Speed',
    legend_title='Metrics',
)

# Display the hourly traffic plot in Streamlit
st.plotly_chart(fig_hourly)
st.markdown("*As Traffic volume increases, the average speed tends to decrease, which aligns with common traffic congestion patterns*")
# Part 2: Weather Condition Analysis (Bar Plot)

# Group by weather condition to analyze average vehicle count and average speed
weather_analysis = df.groupby('weather_condition').agg({
    'vehicle_count': 'mean',
    'average_speed': 'mean'
}).reset_index()

# Create a Plotly bar chart for average vehicle count by weather condition
fig_weather = go.Figure()

# Add bar for Vehicle Count by Weather Condition
fig_weather.add_trace(go.Bar(
    x=weather_analysis['weather_condition'],
    y=weather_analysis['vehicle_count'],
    name='Vehicle Count',
    marker_color='blue'
))

# Update layout with title, labels, rotation for x-axis labels, and gridlines for weather analysis
fig_weather.update_layout(
    title='Average Vehicle Count by Weather Condition',
    xaxis_title='Weather Condition',
    yaxis_title='Average Vehicle Count',
    xaxis_tickangle=-45,
    template='plotly_white'
)

# Display the weather condition plot in Streamlit
st.plotly_chart(fig_weather)




image_path = "./Picture1.jpg"  # Adjust the path if needed
img = Image.open(image_path)
st.image(img, caption="Power_BI_Dasboard", use_container_width=True)
