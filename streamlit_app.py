# streamlit_app.py
import streamlit as st
from main import number_guess

# Streamlit interface
st.title("Guess the Number Game")

# Start the game
if st.button("Start Game"):
    number_guess()  # Call the existing number_guess() function from main.py
