import streamlit as st
import requests
import json

# Title of the page
st.title("🎓 DunkinOrStarbucks")

# Get user inputs
comment  =st.text_input("Comment", help ="paste your comment here to check whether it belongs to Dunkin or Starbucks subreddit" )


# Display the inputs
user_input = {"comment":comment}
st.write("User input:")
st.write(user_input)

# Code to post the user inputs to the API and get the predictions
# Paste the URL to your GCP Cloud Run API here!
api_url = 'https://dunkinorstarbucks-jqjv2zme2q-as.a.run.app'
api_route = '/predict'

response = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input)) # json.dumps() converts dict to JSON
predictions = response.json()

# Add a submit button
if st.button("Submit"): 
    st.write(f"Prediction: {predictions['predictions'][0]}")
