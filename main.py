import glob
import streamlit as st
import plotly.express as px
import pandas as pd

from nltk.sentiment import SentimentIntensityAnalyzer

# File paths list
filepaths = sorted(glob.glob("diary/*.txt"))

analyzer = SentimentIntensityAnalyzer()
negativity = []
positivity = []

# Loop over all file paths in list
for filepath in filepaths:
    #for each file creating a file object
     with open(filepath) as file:
         # reading the content and storing in the content variable
         content = file.read()
     # Calculating the scores for each content  give the dictionary of score contain negativity and positivity of each content
     scores = analyzer.polarity_scores(content)
     # storing the positivity score
     positivity.append(scores["pos"])
     # storing the negativity score
     negativity.append(scores["neg"])
# Extracting date from the filepath name
dates = [name.strip(".txt").strip("diary/") for name in filepaths]

# Create DataFrame
df = pd.DataFrame({
    "Date": dates,
    "Positivity": positivity,
    "Negativity": negativity
})


# Streamlit UI
st.title("Diary Tone")

st.subheader("Positivity")
pos_figure = px.line(df, x="Date", y="Positivity", title="Positivity Over Time")
st.plotly_chart(pos_figure)

st.subheader("Negativity")
neg_figure = px.line(df, x="Date", y="Negativity", title="Negativity Over Time")
st.plotly_chart(neg_figure)

