# Hongfei Luo BSTA040 Final Project
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
import streamlit as st

# Title of the project
st.title('Influenza-like Illess from 2010 to 2025')

# Read in the csv file
ilidata = pd.read_csv('https://raw.githubusercontent.com/FiFi-Luo/BSTA040-Final/refs/heads/main/ilidata.csv')

# Create dataframe df
df = pd.DataFrame(ilidata)

# Add column 'weeks' to the dataframe
df['weeks'] = df['epiweek'].rank(method='dense').astype(int) - 1

# Get the list of state names
states = df['state'].unique()

# Select a state
selected_state = st.selectbox(
    'Please select a state',
    options = states,
    index = 0,
)
selected_state_data = df[df['state'] == selected_state]

# Plot the line chart
st.header('ILI Percentage over time') # Header for the line chart
st.line_chart(
    selected_state_data,
    x = 'weeks',
    y = 'ili',
    x_label = 'Weeks',
    y_label = 'ILI Percentage'
)

# Line chart description
line_explain = '''
This line chart displays the ILI percentage from 2010 to 2025 for the state you selected. 
Each data point represents the ILI percentage for a specific epidemiological week. 

All states exhibit a similar pattern.
Each year, the ILI percentage experiences a sharp peak during the flu season, while remaining relatively low during other times of the year. 
'''
st.markdown(line_explain)

# Plot the histogram
st.header('Histogram of ILI Percentage with its Estimated Exponential Density') # Header for the histogram
fig,ax  = plt.subplots()
ax.hist(df['ili'], bins = 20, density = True)

# Overlay the estimated exponential density
x_grid = np.linspace(0, 20, 1000)
y_mean = np.mean(df['ili']) # This is the lambda parameter for our exponential density
ax.plot(x_grid, expon.pdf(x_grid, scale = y_mean))

# Add labels and title
ax.set_xlabel('ILI Percentage Values')
ax.set_ylabel('Density')
st.pyplot(fig)

# Histogram description
hist_explain = '''
This histogram displays the ILI percentage values along with their estimated probability density. 
The width of each bar represents the range of the ILI percentages, while the height of each bar indicates its corresponding true probability density.

Each ILI value is assumed to be drawn independently from the same exponential distribution. 
The parameter of the exponential distribution used to generate the orange curve is the sample average, which provides an estimate of the expected value of the ILI percentages. 
On this graph, the histogram aligns well with the curve, suggesting the ILI values may be effectively modeled by the estimated exponential density. The probability of having small ILI values is high, while the probability of larger ILI values decreases exponentially.
'''
st.markdown(hist_explain)

# Name and contact
st.write('Author: Hongfei Luo')
st.write('Contact: hluoao@connect.ust.hk')