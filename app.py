import streamlit as st

# Set the title of the app
st.title("Welcome to ACM-CEG's Report Analyser!")
st.write("Hey! This tool helps you quickly pull insights from our feedback forms so that members of the HR domain can make expressive reports fast + events domain can get action points to be implemented in further events")

light_mode_logo = "white_mode.jpeg"  # Replace with your light mode logo path
st.logo(light_mode_logo)
st.markdown("<div style='height: 10pc;'></div>", unsafe_allow_html=True)  # Adjust height as needed

# Made with ❤️ section
st.markdown("---")  # Optional: Adds a horizontal line for separation
st.write("Made with ❤️ by Sharada for ACM-CEG!")
st.write("Thanks to everyone who contributed!")
